# Project Structure

```
setuapi/
├── main.py              # FastAPI application (system endpoints) and router includes
├── database.py          # SQLAlchemy database models and session management
├── schemas.py           # Pydantic models for request/response validation
├── crud_patient.py      # CRUD operations for Patient entity
├── routers/             # API route handlers organized by domain
│   ├── __init__.py      # Routers package
│   └── patients.py      # Patient-specific endpoints router
├── create_tables.sql    # SQL script to create database tables
├── requirements.txt     # Python dependencies
├── env.example          # Environment variables template
├── README.md            # Project documentation
└── .gitignore          # Git ignore rules
```

## File Descriptions

### main.py
- FastAPI application entry point
- Registers routers from the routers package
- Handles request routing and dependency injection

### routers/
- Package containing all API route handlers

### routers/patients.py
- APIRouter with patient-specific endpoints (create, read, update, delete, search)

### database.py
- SQLAlchemy ORM models
- Database session management
- Connection configuration

### schemas.py
- Pydantic models for request/response validation
- PatientCreate, PatientUpdate, PatientResponse schemas

### crud_patient.py
- Database operations (Create, Read, Update, Delete)
- Search functionality
- Pagination support

### create_tables.sql
- SQL script to create patient table
- Includes indexes for better performance

### requirements.txt
- FastAPI
- Uvicorn
- SQLAlchemy
- psycopg2-binary
- python-dotenv

## API Endpoints Summary

### System
- GET / - Root
- GET /health - Health check
- GET /ping - Ping

### Patients
- POST /patients - Create patient
- GET /patients - List all patients
- GET /patients/{id} - Get patient by ID
- PUT /patients/{id} - Update patient
- DELETE /patients/{id} - Delete patient
- GET /patients/search/{term} - Search patients

