from datetime import date
from sqlalchemy import Boolean, Column, Integer, String, Date, Text
from database import Base


class Patient(Base):
    __tablename__ = "patients"

    patient_id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=True)
    age_type = Column(String(10), nullable=True)
    village_id = Column(Integer, nullable=True)
    gender = Column(String(10), nullable=True)
    date_of_birth = Column(Date, nullable=True)
    mobile_number = Column(String(15), nullable=True)
    address = Column(String(255), nullable=True)
    photo_url = Column(String(255), nullable=True)
    created_by = Column(Integer, nullable=False)
    updated_by = Column(Integer, nullable=False)
    created_at = Column(Date, nullable=False, default=date.today)
    updated_at = Column(Date, nullable=False, default=date.today, onupdate=date.today)
    isActive = Column(Boolean, nullable=False, default=True)
