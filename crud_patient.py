from sqlalchemy.orm import Session
from sqlalchemy import and_, or_
from typing import List, Optional
from database import Patient
from schemas import PatientCreate, PatientUpdate


def get_patient(db: Session, patient_id: int) -> Optional[Patient]:
    """Get a single patient by ID"""
    return db.query(Patient).filter(Patient.patient_id == patient_id).first()


def get_all_patients(db: Session, skip: int = 0, limit: int = 100) -> List[Patient]:
    """Get all patients with pagination"""
    return db.query(Patient).offset(skip).limit(limit).all()


def create_patient(db: Session, patient: PatientCreate) -> Patient:
    """Create a new patient"""
    db_patient = Patient(**patient.dict())
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient


def update_patient(db: Session, patient_id: int, patient: PatientUpdate) -> Optional[Patient]:
    """Update an existing patient"""
    db_patient = get_patient(db, patient_id)
    if not db_patient:
        return None
    
    update_data = patient.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_patient, field, value)
    
    db.commit()
    db.refresh(db_patient)
    return db_patient


def delete_patient(db: Session, patient_id: int) -> bool:
    """Delete a patient by ID"""
    db_patient = get_patient(db, patient_id)
    if not db_patient:
        return False
    
    db.delete(db_patient)
    db.commit()
    return True


def search_patients(db: Session, search_term: str, skip: int = 0, limit: int = 100) -> List[Patient]:
    """Search patients by name or mobile number"""
    return db.query(Patient).filter(
        or_(
            Patient.full_name.ilike(f"%{search_term}%"),
            Patient.mobile_number.ilike(f"%{search_term}%")
        )
    ).offset(skip).limit(limit).all()

