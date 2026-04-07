from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from schemas.patient import PatientCreate, PatientResponse, PatientUpdate
from services.patient_service import (
    create_patient,
    delete_patient,
    get_all_patients,
    get_patient_by_id,
    search_patients,
    update_patient,
)

router = APIRouter(prefix="/patients", tags=["patients"])


@router.post("", response_model=PatientResponse, status_code=status.HTTP_201_CREATED)
def create_patient_endpoint(
    patient: PatientCreate,
    db: Session = Depends(get_db),
):
    return create_patient(db=db, patient_data=patient)


@router.get("", response_model=List[PatientResponse])
def read_patients(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
):
    return get_all_patients(db=db, skip=skip, limit=limit)


@router.get("/{patient_id}", response_model=PatientResponse)
def read_patient(patient_id: int, db: Session = Depends(get_db)):
    patient = get_patient_by_id(db=db, patient_id=patient_id)
    if patient is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Patient with ID {patient_id} not found",
        )
    return patient


@router.put("/{patient_id}", response_model=PatientResponse)
def update_patient_endpoint(
    patient_id: int,
    patient: PatientUpdate,
    db: Session = Depends(get_db),
):
    updated_patient = update_patient(db=db, patient_id=patient_id, patient_data=patient)
    if updated_patient is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Patient with ID {patient_id} not found",
        )
    return updated_patient


@router.delete("/{patient_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_patient_endpoint(patient_id: int, db: Session = Depends(get_db)):
    if not delete_patient(db=db, patient_id=patient_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Patient with ID {patient_id} not found",
        )
    return None


@router.get("/search/{search_term}", response_model=List[PatientResponse])
def search_patients_endpoint(
    search_term: str,
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
):
    return search_patients(db=db, search_term=search_term, skip=skip, limit=limit)
