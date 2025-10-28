# SETU Patient API

A RESTful API for managing patient records with PostgreSQL database.

## Setup

1. Install dependencies:
```powershell
pip install -r requirements.txt
```

2. Configure database:
   - Copy `env.example` to `.env`
   - Update the `DATABASE_URL` in `.env` with your PostgreSQL connection details:
   ```
   DATABASE_URL=postgresql://username:password@localhost:5432/database_name
   ```
   - Create the database tables by running `create_tables.sql` in your PostgreSQL database, or let the application create them automatically on startup

3. Run the server:
```powershell
# Option 1: Direct command
uvicorn main:app --reload

# Option 2: Using Python module (recommended for PowerShell)
python -m uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## Endpoints

### System Endpoints
- `GET /` - Root endpoint
- `GET /health` - Health check endpoint
- `GET /ping` - Ping endpoint (returns pong)

### Patient Endpoints
- `POST /patients` - Create a new patient record
- `GET /patients` - Get all patients (with pagination)
- `GET /patients/{patient_id}` - Get a specific patient by ID
- `PUT /patients/{patient_id}` - Update a patient record
- `DELETE /patients/{patient_id}` - Delete a patient record
- `GET /patients/search/{search_term}` - Search patients by name or mobile number

## API Documentation

Once the server is running, you can access the interactive API documentation at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Database Schema

The patient table includes the following fields:
- `patient_id` (Primary Key)
- `full_name` (Required)
- `gender`
- `date_of_birth`
- `age`
- `mobile_number`
- `address`
- `photo_url`
- `created_by` (Required)
- `updated_by` (Required)
- `created_at` (Timestamp)
- `updated_at` (Timestamp)

## Example API Calls

### Create Patient
```bash
POST http://localhost:8000/patients
Content-Type: application/json

{
  "full_name": "John Doe",
  "gender": "Male",
  "date_of_birth": "1990-01-15",
  "age": 33,
  "mobile_number": "+1234567890",
  "address": "123 Main St",
  "photo_url": "https://example.com/photo.jpg",
  "created_by": 1,
  "updated_by": 1
}
```

### Get All Patients
```bash
GET http://localhost:8000/patients?skip=0&limit=10
```

### Update Patient
```bash
PUT http://localhost:8000/patients/1
Content-Type: application/json

{
  "full_name": "John Smith",
  "updated_by": 1
}
```

### Delete Patient
```bash
DELETE http://localhost:8000/patients/1
```
