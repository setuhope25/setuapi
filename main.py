from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from database import init_db, SessionLocal
from routers.patient_router import router as patient_router
from setumock import router as mock_router
from datetime import datetime


app = FastAPI(
    title="SETU Patient API",
    description="API for managing patient records",
    version="1.0.0"
)

# Configure CORS for frontend compatibility
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    """Initialize database on startup"""
    try:
        init_db()
    except Exception as e:
        print(f"Database initialization failed: {e}")
        print("API will run without database connection")


# Include patient router
app.include_router(patient_router)

# Include mock API router
app.include_router(mock_router)


@app.get("/")
def root():
    return {"message": "Welcome to the SETU API"}


@app.get("/health")
def health_check():
    """
    Health check endpoint that verifies database connectivity.
    Returns detailed status information about the API and database connection.
    """
    health_status = {
        "status": "unhealthy",
        "service": "SETU Patient API",
        "timestamp": datetime.utcnow().isoformat(),
        "database": {
            "connected": False,
            "message": "Not connected"
        },
        "api": {
            "running": True
        }
    }
    
    try:
        db = SessionLocal()
        result = db.execute(text("SELECT * from village"))
        village_row = result.fetchone()

        db_info = db.execute(text("SELECT current_database(), current_user, version()"))
        db_row = db_info.fetchone()

        db.close()

        health_status["status"] = "healthy"
        health_status["database"]["connected"] = True
        health_status["database"]["message"] = "Connected to PostgreSQL"

        if db_row:
            health_status["database"]["database_name"] = db_row[0]
            health_status["database"]["user"] = db_row[1]
            health_status["database"]["version"] = db_row[2]
            health_status["database"]["village_table_sample"] = {
                "id": village_row[0],
                "name": village_row[1]
            } if village_row else "No data in village table"

    except Exception as e:
        health_status["status"] = "degraded"
        health_status["database"] = {
            "connected": False,
            "message": f"Connection failed: {str(e)}"
        }
        health_status["error_details"] = str(e)
    
    return health_status


@app.get("/ping")
def ping():
    return {"message": "pong"}


