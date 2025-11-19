from fastapi import FastAPI
from database import init_db
from routers.patients import router as patient_router


app = FastAPI(
    title="SETU Patient API",
    description="API for managing patient records",
    version="1.0.0"
)


@app.on_event("startup")
async def startup_event():
    """Initialize database on startup"""
    try:
        init_db()
    except Exception as e:
        print(f"Database initialization failed: {e}")
        print("API will run without database connection")


# include patient router
app.include_router(patient_router)


@app.get("/")
def root():
    return {"message": "Welcome to the SETU  API"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/ping")
def ping():
    return {"message": "pong"}


