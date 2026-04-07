from datetime import date
from typing import List, Optional
from sqlalchemy import or_
from sqlalchemy.orm import Session
from models.patient import Patient
from schemas.patient import PatientCreate, PatientUpdate


def create_patient(db: Session, patient_data: PatientCreate) -> Patient:
    db_patient = Patient(**patient_data.dict(), isActive=True)
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient


def get_all_patients(db: Session, skip: int = 0, limit: int = 10) -> List[Patient]:
    return db.query(Patient).filter(Patient.isActive == True).offset(skip).limit(limit).all()


def get_patient_by_id(db: Session, patient_id: int) -> Optional[Patient]:
    return db.query(Patient).filter(Patient.patient_id == patient_id, Patient.isActive == True).first()


def update_patient(db: Session, patient_id: int, patient_data: PatientUpdate) -> Optional[Patient]:
    db_patient = get_patient_by_id(db, patient_id)
    if not db_patient:
        return None

    update_data = patient_data.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_patient, field, value)

    db_patient.updated_at = date.today()
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient


def delete_patient(db: Session, patient_id: int) -> bool:
    db_patient = get_patient_by_id(db, patient_id)
    if not db_patient:
        return False

    db_patient.isActive = False
    db.commit()
    return True


def search_patients(db: Session, search_term: str, skip: int = 0, limit: int = 10) -> List[Patient]:
    search_pattern = f"%{search_term}%"
    return (
        db.query(Patient)
        .filter(
            Patient.isActive == True,
            or_(
                Patient.full_name.ilike(search_pattern),
                Patient.mobile_number.ilike(search_pattern),
            )
        )
        .offset(skip)
        .limit(limit)
        .all()
    )
