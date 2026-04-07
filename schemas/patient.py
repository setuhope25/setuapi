from datetime import date
from typing import Optional
from pydantic import BaseModel, Field


class PatientBase(BaseModel):
    full_name: str = Field(..., max_length=100)
    age: Optional[int] = None
    age_type: Optional[str] = Field(None, max_length=10)
    village_id: Optional[int] = None
    gender: Optional[str] = Field(None, max_length=10)
    date_of_birth: Optional[date] = None
    mobile_number: Optional[str] = Field(None, max_length=15)
    address: Optional[str] = Field(None, max_length=255)
    photo_url: Optional[str] = Field(None, max_length=255)
    isActive: Optional[bool] = True


class PatientCreate(PatientBase):
    created_by: int
    updated_by: int


class PatientUpdate(BaseModel):
    full_name: Optional[str] = Field(None, max_length=100)
    age: Optional[int] = None
    age_type: Optional[str] = Field(None, max_length=10)
    village_id: Optional[int] = None
    gender: Optional[str] = Field(None, max_length=10)
    date_of_birth: Optional[date] = None
    mobile_number: Optional[str] = Field(None, max_length=15)
    address: Optional[str] = Field(None, max_length=255)
    photo_url: Optional[str] = Field(None, max_length=255)
    updated_by: Optional[int] = None


class PatientResponse(PatientBase):
    patient_id: int
    created_by: Optional[int] = None
    updated_by: Optional[int] = None
    created_at: Optional[date] = None
    updated_at: Optional[date] = None
    isActive: bool = True

    model_config = {
        "from_attributes": True,
    }
