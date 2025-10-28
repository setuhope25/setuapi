from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from database import get_db, init_db
from schemas import PatientCreate, PatientUpdate, PatientResponse
import crud

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


@app.get("/")
def root():
    return {"message": "Welcome to the SETU  API"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/ping")
def ping():
    return {"message": "pong"}


# Patient Endpoints

@app.post("/patients", response_model=PatientResponse, status_code=status.HTTP_201_CREATED)
def create_patient(patient: PatientCreate, db: Session = Depends(get_db)):
    """Create a new patient record"""
    return crud.create_patient(db=db, patient=patient)


@app.get("/patients", response_model=List[PatientResponse])
def get_all_patients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all patients with pagination"""
    try:
        patients = crud.get_all_patients(db=db, skip=skip, limit=limit)
        return patients
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {str(e)}"
        )


@app.get("/patients/{patient_id}", response_model=PatientResponse)
def get_patient(patient_id: int, db: Session = Depends(get_db)):
    """Get a specific patient by ID"""
    patient = crud.get_patient(db=db, patient_id=patient_id)
    if patient is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Patient with ID {patient_id} not found"
        )
    return patient


@app.put("/patients/{patient_id}", response_model=PatientResponse)
def update_patient(patient_id: int, patient: PatientUpdate, db: Session = Depends(get_db)):
    """Update an existing patient record"""
    updated_patient = crud.update_patient(db=db, patient_id=patient_id, patient=patient)
    if updated_patient is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Patient with ID {patient_id} not found"
        )
    return updated_patient


@app.delete("/patients/{patient_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_patient(patient_id: int, db: Session = Depends(get_db)):
    """Delete a patient record"""
    success = crud.delete_patient(db=db, patient_id=patient_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Patient with ID {patient_id} not found"
        )
    return None


@app.get("/patients/search/{search_term}", response_model=List[PatientResponse])
def search_patients(search_term: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Search patients by name or mobile number"""
    patients = crud.search_patients(db=db, search_term=search_term, skip=skip, limit=limit)
    return patients

