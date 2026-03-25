from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import init_db
from routers.patients import router as patient_router
from setumock import router as mock_router


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
    return {"message": "Welcome to the SETU  API"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/ping")
def ping():
    return {"message": "pong"}


