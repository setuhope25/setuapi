"""
Mock API Endpoints for SetuSathi Application
This file provides in-memory mock implementations of all API endpoints.
Used for frontend development and testing before PostgreSQL integration.
"""

import logging
from datetime import datetime, date
from typing import List, Optional, Dict, Any
from uuid import uuid4
import uuid as uuid_module
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field

# Configure logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create router with /mock prefix
router = APIRouter(prefix="/mock", tags=["mock"])

# ============================================================================
#                          PYDANTIC MODELS
# ============================================================================

# --- Auth & User Models ---
class LoginRequest(BaseModel):
    email: str
    password: str


class LoginResponse(BaseModel):
    success: bool
    user: Dict[str, Any]
    access_token: str


class RegisterRequest(BaseModel):
    full_name: str
    member_id: str
    email: str
    mobile: str
    password: str
    role: str = "doctor"
    photo_url: Optional[str] = None


class RegisterResponse(BaseModel):
    success: bool
    user: Dict[str, Any]


class UserProfile(BaseModel):
    id: str
    full_name: str
    member_id: str
    email: str
    mobile: str
    photo_url: Optional[str] = None
    role: str


class UpdateUserRequest(BaseModel):
    mobile: Optional[str] = None
    photo_url: Optional[str] = None
    full_name: Optional[str] = None


class UpdateUserResponse(BaseModel):
    success: bool
    user: UserProfile


class ForgotPasswordRequest(BaseModel):
    email: str


class ForgotPasswordResponse(BaseModel):
    success: bool
    message: str


# --- Patient Models ---
class PatientMockBase(BaseModel):
    full_name: str
    gender: Optional[str] = None
    date_of_birth: Optional[date] = None
    age: Optional[int] = None
    mobile_number: Optional[str] = None
    address: Optional[str] = None
    photo_url: Optional[str] = None


class PatientMockCreate(PatientMockBase):
    created_by: int
    updated_by: int


class PatientMockUpdate(BaseModel):
    full_name: Optional[str] = None
    gender: Optional[str] = None
    date_of_birth: Optional[date] = None
    age: Optional[int] = None
    mobile_number: Optional[str] = None
    address: Optional[str] = None
    photo_url: Optional[str] = None
    updated_by: int


class PatientMockResponse(PatientMockBase):
    patient_id: int
    created_by: Optional[int] = None
    updated_by: Optional[int] = None
    created_at: datetime
    updated_at: datetime


# --- OPD Session Models ---
class OPDSessionStartRequest(BaseModel):
    opd_id: str
    pin: str
    village: str
    desk_role: str
    created_by: str


class OPDSessionStartResponse(BaseModel):
    success: bool
    opd_id: str
    pin: str


class OPDPatientItem(BaseModel):
    id: str
    name: str
    gender: str
    age: int
    token: int
    status: Optional[str] = "waiting"
    notes: Optional[str] = None


class OPDSessionResponse(BaseModel):
    opd_id: str
    pin: str
    village: str
    desk_role: str
    status: str
    patients: List[OPDPatientItem]
    created_at: datetime


class OPDStatsResponse(BaseModel):
    totalOPDs: int
    vitalsRecorded: int
    consultsDone: int
    medicinesGiven: int


class UpdatePatientStatusRequest(BaseModel):
    status: str
    notes: Optional[str] = None


class UpdatePatientStatusResponse(BaseModel):
    success: bool
    patient: OPDPatientItem


# --- Clinical Models ---
class RecordVitalsRequest(BaseModel):
    temp: Optional[str] = None
    pulse: Optional[str] = None
    bp: Optional[str] = None
    spo2: Optional[str] = None
    blood_sugar: Optional[str] = None
    allergies: Optional[str] = None
    notes: Optional[str] = None


class RecordVitalsResponse(BaseModel):
    success: bool
    vitals_id: int


class RecordConsultRequest(BaseModel):
    diagnosis: List[str]
    lab_tests: List[str]
    follow_up: str
    doctor_notes: str


class RecordConsultResponse(BaseModel):
    success: bool
    consult_id: int


class MedicineItem(BaseModel):
    id: str
    name: str
    dosage: str
    days: int
    timing: str


class DispenseMedicinesRequest(BaseModel):
    medicines: List[MedicineItem]


class DispenseMedicinesResponse(BaseModel):
    success: bool
    dispense_id: int


class PatientHistoryVitals(BaseModel):
    temp: Optional[str] = None
    bp: Optional[str] = None
    pulse: Optional[str] = None
    bs: Optional[str] = None
    spo2: Optional[str] = None


class PatientHistoryItem(BaseModel):
    id: str
    date: date
    consulted_by: str
    complaints: List[str]
    vitals: PatientHistoryVitals
    allergies: Optional[str]
    registration_notes: Optional[str]
    vitals_notes: Optional[str]
    diagnosis: List[str]
    lab_tests: List[str]
    medicines: List[MedicineItem]


# ============================================================================
#                          IN-MEMORY DATA STORAGE
# ============================================================================

# Mock data stores
users_db: Dict[str, Dict[str, Any]] = {
    "u_123": {
        "id": "u_123",
        "full_name": "Dr. Demo",
        "member_id": "D0001",
        "email": "doctor@setu.test",
        "mobile": "9876543210",
        "password": "secret123",
        "role": "doctor",
        "photo_url": "https://api.example.com/photos/doctor.jpg"
    },
    "u_124": {
        "id": "u_124",
        "full_name": "Dr. Asha Patel",
        "member_id": "D0024",
        "email": "asha@setu.test",
        "mobile": "9876543210",
        "password": "secret123",
        "role": "doctor",
        "photo_url": "https://api.example.com/photos/asha.jpg"
    }
}

patients_db: Dict[int, Dict[str, Any]] = {
    1: {
        "patient_id": 1,
        "full_name": "John Doe",
        "gender": "Male",
        "date_of_birth": date(1990, 1, 15),
        "age": 33,
        "mobile_number": "+1234567890",
        "address": "123 Main St",
        "photo_url": "https://example.com/photo.jpg",
        "created_by": 1,
        "updated_by": 1,
        "created_at": datetime(2024, 6, 1, 12, 0, 0),
        "updated_at": datetime(2024, 6, 1, 12, 0, 0)
    },
    2: {
        "patient_id": 2,
        "full_name": "Dharamshinhbhai Prajapati",
        "gender": "Male",
        "date_of_birth": date(1965, 5, 20),
        "age": 58,
        "mobile_number": "+9876543210",
        "address": "Ramagri Village",
        "photo_url": None,
        "created_by": 1,
        "updated_by": 1,
        "created_at": datetime(2024, 6, 2, 9, 30, 0),
        "updated_at": datetime(2024, 6, 2, 9, 30, 0)
    }
}

opd_sessions_db: Dict[str, Dict[str, Any]] = {}

vitals_db: Dict[int, Dict[str, Any]] = {}
vitals_counter: int = 500

consultations_db: Dict[int, Dict[str, Any]] = {}
consultations_counter: int = 7000

medicines_db: Dict[int, Dict[str, Any]] = {}
medicines_counter: int = 9000

patient_history_db: Dict[int, List[Dict[str, Any]]] = {
    1: [
        {
            "id": "vh-1",
            "date": date(2026, 3, 10),
            "consulted_by": "Dr. Ramesh Jani",
            "complaints": ["Body pain", "Fever"],
            "vitals": {
                "temp": "98.2 F",
                "bp": "140/120",
                "pulse": "86 bpm",
                "bs": "120",
                "spo2": "99"
            },
            "allergies": "Smoke allergy",
            "registration_notes": "Patient felt dizzy earlier",
            "vitals_notes": "BP high",
            "diagnosis": ["Arthritis"],
            "lab_tests": ["CBC"],
            "medicines": [
                {
                    "id": "6.2",
                    "name": "T. Citra",
                    "dosage": "1-0-1",
                    "days": 3,
                    "timing": "After Meal"
                }
            ]
        }
    ]
}

# Counter for patient IDs
patient_id_counter: int = 2
current_user_id: str = "u_124"  # Default logged-in user

# ============================================================================
#                          AUTH & USER PROFILE ENDPOINTS
# ============================================================================

@router.post("/auth/login", response_model=LoginResponse, status_code=status.HTTP_200_OK)
async def login(request: LoginRequest):
    """
    Login endpoint - Authenticate user by email and password
    Returns JWT token and user profile
    """
    logger.info(f"Login attempt for email: {request.email}")

    # Mock authentication
    user = None
    for user_id, u in users_db.items():
        if u["email"] == request.email and u["password"] == request.password:
            user = u
            break

    if not user:
        logger.warning(f"Login failed for email: {request.email}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    # Generate mock JWT token
    token = f"jwt_token_{user['id']}_{uuid4()}"

    user_response = {
        "id": user["id"],
        "full_name": user["full_name"],
        "member_id": user["member_id"],
        "email": user["email"],
        "mobile": user["mobile"],
        "role": user["role"]
    }

    logger.info(f"Login successful for user: {user['id']}")

    return LoginResponse(
        success=True,
        user=user_response,
        access_token=token
    )


@router.post("/auth/register", response_model=RegisterResponse, status_code=status.HTTP_201_CREATED)
async def register(request: RegisterRequest):
    """
    Register new doctor/volunteer
    Stores user in mock database
    """
    logger.info(f"Registration attempt for email: {request.email}")

    # Check if email already exists
    for user in users_db.values():
        if user["email"] == request.email:
            logger.warning(f"Registration failed - email exists: {request.email}")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )

    # Create new user
    user_id = f"u_{int(uuid_module.uuid4().int % 10000)}"
    new_user = {
        "id": user_id,
        "full_name": request.full_name,
        "member_id": request.member_id,
        "email": request.email,
        "mobile": request.mobile,
        "password": request.password,
        "role": request.role,
        "photo_url": request.photo_url
    }

    users_db[user_id] = new_user

    logger.info(f"User registered successfully: {user_id}")

    user_response = {
        "id": new_user["id"],
        "full_name": new_user["full_name"],
        "member_id": new_user["member_id"],
        "email": new_user["email"],
        "mobile": new_user["mobile"],
        "role": new_user["role"],
        "photo_url": new_user["photo_url"]
    }

    return RegisterResponse(success=True, user=user_response)


@router.post("/auth/forgot-password", response_model=ForgotPasswordResponse, status_code=status.HTTP_200_OK)
async def forgot_password(request: ForgotPasswordRequest):
    """
    Send password reset link to user's email
    """
    logger.info(f"Forgot password request for email: {request.email}")

    # Check if email exists
    user_exists = any(u["email"] == request.email for u in users_db.values())

    if not user_exists:
        # Return success even if email doesn't exist (security best practice)
        logger.warning(f"Forgot password request for non-existent email: {request.email}")

    logger.info(f"Reset link would be sent to: {request.email}")

    return ForgotPasswordResponse(
        success=True,
        message="Password reset link sent to your email. Check your inbox."
    )


@router.get("/users/me", response_model=UserProfile, status_code=status.HTTP_200_OK)
async def get_current_user():
    """
    Get current logged-in user's profile
    """
    logger.info(f"Fetching user profile for: {current_user_id}")

    user = users_db.get(current_user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return UserProfile(
        id=user["id"],
        full_name=user["full_name"],
        member_id=user["member_id"],
        email=user["email"],
        mobile=user["mobile"],
        photo_url=user["photo_url"],
        role=user["role"]
    )


@router.patch("/users/me", response_model=UpdateUserResponse, status_code=status.HTTP_200_OK)
async def update_current_user(request: UpdateUserRequest):
    """
    Update current user's profile
    """
    logger.info(f"Updating user profile for: {current_user_id}")

    user = users_db.get(current_user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    # Update fields
    if request.mobile:
        user["mobile"] = request.mobile
    if request.photo_url:
        user["photo_url"] = request.photo_url
    if request.full_name:
        user["full_name"] = request.full_name

    logger.info(f"User profile updated: {current_user_id}")

    user_profile = UserProfile(
        id=user["id"],
        full_name=user["full_name"],
        member_id=user["member_id"],
        email=user["email"],
        mobile=user["mobile"],
        photo_url=user["photo_url"],
        role=user["role"]
    )

    return UpdateUserResponse(success=True, user=user_profile)


# ============================================================================
#                          PATIENT ENDPOINTS (MOCK)
# ============================================================================

@router.post("/patients", response_model=PatientMockResponse, status_code=status.HTTP_201_CREATED)
async def create_patient(patient: PatientMockCreate):
    """
    Create a new patient record
    """
    global patient_id_counter

    logger.info(f"Creating new patient: {patient.full_name}")

    patient_id_counter += 1
    new_patient = {
        "patient_id": patient_id_counter,
        "full_name": patient.full_name,
        "gender": patient.gender,
        "date_of_birth": patient.date_of_birth,
        "age": patient.age,
        "mobile_number": patient.mobile_number,
        "address": patient.address,
        "photo_url": patient.photo_url,
        "created_by": patient.created_by,
        "updated_by": patient.updated_by,
        "created_at": datetime.now(),
        "updated_at": datetime.now()
    }

    patients_db[patient_id_counter] = new_patient

    logger.info(f"Patient created with ID: {patient_id_counter}")

    return PatientMockResponse(**new_patient)


@router.get("/patients", response_model=List[PatientMockResponse], status_code=status.HTTP_200_OK)
async def get_all_patients(skip: int = 0, limit: int = 100):
    """
    Get all patients with pagination
    """
    logger.info(f"Fetching patients - skip: {skip}, limit: {limit}")

    patients_list = list(patients_db.values())[skip:skip + limit]
    return [PatientMockResponse(**p) for p in patients_list]


@router.get("/patients/{patient_id}", response_model=PatientMockResponse, status_code=status.HTTP_200_OK)
async def get_patient(patient_id: int):
    """
    Get a specific patient by ID
    """
    logger.info(f"Fetching patient: {patient_id}")

    patient = patients_db.get(patient_id)
    if not patient:
        logger.warning(f"Patient not found: {patient_id}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Patient with ID {patient_id} not found"
        )

    return PatientMockResponse(**patient)


@router.put("/patients/{patient_id}", response_model=PatientMockResponse, status_code=status.HTTP_200_OK)
async def update_patient(patient_id: int, patient: PatientMockUpdate):
    """
    Update an existing patient record
    """
    logger.info(f"Updating patient: {patient_id}")

    if patient_id not in patients_db:
        logger.warning(f"Patient not found for update: {patient_id}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Patient with ID {patient_id} not found"
        )

    existing_patient = patients_db[patient_id]

    # Update fields
    if patient.full_name:
        existing_patient["full_name"] = patient.full_name
    if patient.gender:
        existing_patient["gender"] = patient.gender
    if patient.date_of_birth:
        existing_patient["date_of_birth"] = patient.date_of_birth
    if patient.age:
        existing_patient["age"] = patient.age
    if patient.mobile_number:
        existing_patient["mobile_number"] = patient.mobile_number
    if patient.address:
        existing_patient["address"] = patient.address
    if patient.photo_url:
        existing_patient["photo_url"] = patient.photo_url

    existing_patient["updated_by"] = patient.updated_by
    existing_patient["updated_at"] = datetime.now()

    logger.info(f"Patient updated: {patient_id}")

    return PatientMockResponse(**existing_patient)


@router.delete("/patients/{patient_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_patient(patient_id: int):
    """
    Delete a patient record
    """
    logger.info(f"Deleting patient: {patient_id}")

    if patient_id not in patients_db:
        logger.warning(f"Patient not found for deletion: {patient_id}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Patient with ID {patient_id} not found"
        )

    del patients_db[patient_id]

    logger.info(f"Patient deleted: {patient_id}")

    return None


@router.get("/patients/search/{search_term}", response_model=List[PatientMockResponse], status_code=status.HTTP_200_OK)
async def search_patients(search_term: str, skip: int = 0, limit: int = 100):
    """
    Search patients by name or mobile number
    """
    logger.info(f"Searching patients for term: {search_term}")

    results = []
    search_lower = search_term.lower()

    for patient in patients_db.values():
        if (search_lower in patient["full_name"].lower() or
            (patient["mobile_number"] and search_lower in patient["mobile_number"])):
            results.append(patient)

    paginated_results = results[skip:skip + limit]

    logger.info(f"Search returned {len(paginated_results)} results")

    return [PatientMockResponse(**p) for p in paginated_results]


# ============================================================================
#                          OPD SESSION ENDPOINTS
# ============================================================================

@router.post("/opd/sessions", response_model=OPDSessionStartResponse, status_code=status.HTTP_201_CREATED)
async def start_opd_session(request: OPDSessionStartRequest):
    """
    Start a new OPD session with PIN
    """
    logger.info(f"Starting OPD session: {request.opd_id}")

    if request.pin in opd_sessions_db:
        logger.warning(f"OPD session PIN already exists: {request.pin}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="PIN already in use"
        )

    new_session = {
        "opd_id": request.opd_id,
        "pin": request.pin,
        "village": request.village,
        "desk_role": request.desk_role,
        "created_by": request.created_by,
        "status": "active",
        "patients": [],
        "created_at": datetime.now()
    }

    opd_sessions_db[request.pin] = new_session

    logger.info(f"OPD session created with PIN: {request.pin}")

    return OPDSessionStartResponse(
        success=True,
        opd_id=request.opd_id,
        pin=request.pin
    )


@router.get("/opd/sessions/{pin}", response_model=OPDSessionResponse, status_code=status.HTTP_200_OK)
async def get_opd_session(pin: str):
    """
    Get OPD session details by PIN
    """
    logger.info(f"Fetching OPD session for PIN: {pin}")

    session = opd_sessions_db.get(pin)
    if not session:
        logger.warning(f"OPD session not found: {pin}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"OPD session with PIN {pin} not found"
        )

    return OPDSessionResponse(
        opd_id=session["opd_id"],
        pin=session["pin"],
        village=session["village"],
        desk_role=session["desk_role"],
        status=session["status"],
        patients=[OPDPatientItem(**p) for p in session["patients"]],
        created_at=session["created_at"]
    )


@router.post("/opd/sessions/{pin}/patients", response_model=dict, status_code=status.HTTP_201_CREATED)
async def add_patient_to_opd(pin: str, patient: OPDPatientItem):
    """
    Add a patient to OPD session queue
    """
    logger.info(f"Adding patient to OPD session {pin}: {patient.name}")

    session = opd_sessions_db.get(pin)
    if not session:
        logger.warning(f"OPD session not found: {pin}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"OPD session with PIN {pin} not found"
        )

    patient_dict = {
        "id": patient.id,
        "name": patient.name,
        "gender": patient.gender,
        "age": patient.age,
        "token": patient.token,
        "status": "waiting",
        "notes": None
    }

    session["patients"].append(patient_dict)

    logger.info(f"Patient added to OPD queue - PIN: {pin}, Patient: {patient.id}")

    return {"success": True}


@router.get("/opd/stats", response_model=OPDStatsResponse, status_code=status.HTTP_200_OK)
async def get_opd_stats():
    """
    Get OPD statistics
    """
    logger.info("Fetching OPD statistics")

    total_opds = len(opd_sessions_db)
    vitals_recorded = len(vitals_db)
    consults_done = len(consultations_db)
    medicines_given = len(medicines_db)

    return OPDStatsResponse(
        totalOPDs=total_opds,
        vitalsRecorded=vitals_recorded,
        consultsDone=consults_done,
        medicinesGiven=medicines_given
    )


@router.patch("/opd/sessions/{pin}/patients/{patient_id}", response_model=UpdatePatientStatusResponse, status_code=status.HTTP_200_OK)
async def update_opd_patient_status(pin: str, patient_id: str, request: UpdatePatientStatusRequest):
    """
    Update OPD patient status (waiting, consulted, completed, etc.)
    """
    logger.info(f"Updating patient status - PIN: {pin}, Patient: {patient_id}, Status: {request.status}")

    session = opd_sessions_db.get(pin)
    if not session:
        logger.warning(f"OPD session not found: {pin}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"OPD session with PIN {pin} not found"
        )

    patient_found = False
    for patient in session["patients"]:
        if patient["id"] == patient_id:
            patient["status"] = request.status
            patient["notes"] = request.notes
            patient_found = True
            break

    if not patient_found:
        logger.warning(f"Patient not found in OPD session: {patient_id}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Patient {patient_id} not found in session"
        )

    logger.info(f"Patient status updated successfully")

    updated_patient = next(p for p in session["patients"] if p["id"] == patient_id)

    return UpdatePatientStatusResponse(
        success=True,
        patient=OPDPatientItem(**updated_patient)
    )


# ============================================================================
#                          CLINICAL ENDPOINTS
# ============================================================================

@router.post("/patients/{patient_id}/vitals", response_model=RecordVitalsResponse, status_code=status.HTTP_201_CREATED)
async def record_vitals(patient_id: int, request: RecordVitalsRequest):
    """
    Record patient vitals (temperature, pulse, BP, etc.)
    """
    global vitals_counter

    logger.info(f"Recording vitals for patient: {patient_id}")

    # Verify patient exists
    if patient_id not in patients_db:
        logger.warning(f"Patient not found for vitals recording: {patient_id}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Patient with ID {patient_id} not found"
        )

    vitals_counter += 1
    vitals_db[vitals_counter] = {
        "vitals_id": vitals_counter,
        "patient_id": patient_id,
        "temp": request.temp,
        "pulse": request.pulse,
        "bp": request.bp,
        "spo2": request.spo2,
        "blood_sugar": request.blood_sugar,
        "allergies": request.allergies,
        "notes": request.notes,
        "recorded_at": datetime.now()
    }

    logger.info(f"Vitals recorded with ID: {vitals_counter}")

    return RecordVitalsResponse(success=True, vitals_id=vitals_counter)


@router.post("/patients/{patient_id}/consult", response_model=RecordConsultResponse, status_code=status.HTTP_201_CREATED)
async def record_consultation(patient_id: int, request: RecordConsultRequest):
    """
    Record consultation details (diagnosis, lab tests, follow-up)
    """
    global consultations_counter

    logger.info(f"Recording consultation for patient: {patient_id}")

    # Verify patient exists
    if patient_id not in patients_db:
        logger.warning(f"Patient not found for consultation: {patient_id}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Patient with ID {patient_id} not found"
        )

    consultations_counter += 1
    consultations_db[consultations_counter] = {
        "consult_id": consultations_counter,
        "patient_id": patient_id,
        "diagnosis": request.diagnosis,
        "lab_tests": request.lab_tests,
        "follow_up": request.follow_up,
        "doctor_notes": request.doctor_notes,
        "consulted_at": datetime.now()
    }

    logger.info(f"Consultation recorded with ID: {consultations_counter}")

    return RecordConsultResponse(success=True, consult_id=consultations_counter)


@router.post("/patients/{patient_id}/medicines", response_model=DispenseMedicinesResponse, status_code=status.HTTP_201_CREATED)
async def dispense_medicines(patient_id: int, request: DispenseMedicinesRequest):
    """
    Dispense medicines to patient
    """
    global medicines_counter

    logger.info(f"Dispensing medicines for patient: {patient_id}")

    # Verify patient exists
    if patient_id not in patients_db:
        logger.warning(f"Patient not found for medicine dispensing: {patient_id}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Patient with ID {patient_id} not found"
        )

    medicines_counter += 1
    medicines_db[medicines_counter] = {
        "dispense_id": medicines_counter,
        "patient_id": patient_id,
        "medicines": [m.dict() for m in request.medicines],
        "dispensed_at": datetime.now()
    }

    logger.info(f"Medicines dispensed with ID: {medicines_counter}")

    return DispenseMedicinesResponse(success=True, dispense_id=medicines_counter)


@router.get("/patients/{patient_id}/history", response_model=List[PatientHistoryItem], status_code=status.HTTP_200_OK)
async def get_patient_history(patient_id: int):
    """
    Get patient's consultation and vitals history
    """
    logger.info(f"Fetching history for patient: {patient_id}")

    # Verify patient exists
    if patient_id not in patients_db:
        logger.warning(f"Patient not found for history retrieval: {patient_id}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Patient with ID {patient_id} not found"
        )

    history = patient_history_db.get(patient_id, [])

    logger.info(f"Retrieved {len(history)} history records for patient: {patient_id}")

    return [PatientHistoryItem(**item) for item in history]


# ============================================================================
#                          HEALTH CHECK ENDPOINT
# ============================================================================

@router.get("/health", status_code=status.HTTP_200_OK)
async def mock_health_check():
    """
    Health check endpoint for mock API
    """
    return {
        "status": "healthy",
        "service": "mock-api",
        "timestamp": datetime.now().isoformat()
    }
