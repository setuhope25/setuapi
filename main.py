from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import init_db, test_database_connection
from routers.patients import router as patient_router
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
    Health check endpoint that verifies Neon PostgreSQL connectivity.
    Returns detailed status information about the API and database connection.
    """
    health_status = {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat()
    }
    
    try:
        # Test database connectivity using psycopg2
        connected, message = test_database_connection()
        
        health_status["database"] = {
            "connected": connected,
            "message": message
        }
        
        if not connected:
            health_status["status"] = "degraded"
        
    except Exception as e:
        health_status["status"] = "degraded"
        health_status["database"] = {
            "connected": False,
            "message": f"Database health check failed: {str(e)}"
        }
    
    return health_status


@app.get("/ping")
def ping():
    return {"message": "pong"}


