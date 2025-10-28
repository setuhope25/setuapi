from pydantic import BaseModel, Field
from datetime import date, datetime
from typing import Optional


class PatientBase(BaseModel):
    full_name: str = Field(..., description="Full name of the patient")
    gender: Optional[str] = Field(None, description="Gender of the patient")
    date_of_birth: Optional[date] = Field(None, description="Date of birth")
    age: Optional[int] = Field(None, description="Age of the patient")
    mobile_number: Optional[str] = Field(None, description="Mobile number")
    address: Optional[str] = Field(None, description="Address of the patient")
    photo_url: Optional[str] = Field(None, description="URL of patient photo")


class PatientCreate(PatientBase):
    created_by: int = Field(..., description="User ID who created the record")
    updated_by: int = Field(..., description="User ID who updated the record")


class PatientUpdate(BaseModel):
    full_name: Optional[str] = None
    gender: Optional[str] = None
    date_of_birth: Optional[date] = None
    age: Optional[int] = None
    mobile_number: Optional[str] = None
    address: Optional[str] = None
    photo_url: Optional[str] = None
    updated_by: int = Field(..., description="User ID who updated the record")


class PatientResponse(PatientBase):
    patient_id: int
    created_by: Optional[int] = None
    updated_by: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

