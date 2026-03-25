# Mock API - curl & Postman Examples

**Base URL**: `http://localhost:8000/mock` or `https://your-api.vercel.app/mock`

---

## Table of Contents
1. [Auth & User Profile](#auth--user-profile)
2. [Patient APIs](#patient-apis)
3. [OPD Session APIs](#opd-session-apis)
4. [Clinical APIs](#clinical-apis)

---

## Auth & User Profile

### 1. Login

**curl**
```bash
curl -X POST "http://localhost:8000/mock/auth/login" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "doctor@setu.test",
    "password": "secret123"
  }'
```

**Response (200 OK)**
```json
{
  "success": true,
  "user": {
    "id": "u_123",
    "full_name": "Dr. Demo",
    "email": "doctor@setu.test",
    "member_id": "D0001",
    "mobile": "9876543210",
    "role": "doctor"
  },
  "access_token": "jwt_token_u_123_..."
}
```

**Postman**
- Method: `POST`
- URL: `{{BASE_URL}}/auth/login`
- Body (JSON):
  ```json
  {
    "email": "doctor@setu.test",
    "password": "secret123"
  }
  ```

---

### 2. Register Doctor/Volunteer

**curl**
```bash
curl -X POST "http://localhost:8000/mock/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "full_name": "Dr. Rajesh Kumar",
    "member_id": "D0025",
    "email": "rajesh@setu.test",
    "mobile": "9999888877",
    "password": "secure123",
    "role": "doctor",
    "photo_url": "https://example.com/rajesh.jpg"
  }'
```

**Response (201 Created)**
```json
{
  "success": true,
  "user": {
    "id": "u_3247",
    "full_name": "Dr. Rajesh Kumar",
    "member_id": "D0025",
    "email": "rajesh@setu.test",
    "mobile": "9999888877",
    "role": "doctor",
    "photo_url": "https://example.com/rajesh.jpg"
  }
}
```

**Postman**
- Method: `POST`
- URL: `{{BASE_URL}}/auth/register`
- Body (JSON):
  ```json
  {
    "full_name": "Dr. Rajesh Kumar",
    "member_id": "D0025",
    "email": "rajesh@setu.test",
    "mobile": "9999888877",
    "password": "secure123",
    "role": "doctor"
  }
  ```

---

### 3. Forgot Password

**curl**
```bash
curl -X POST "http://localhost:8000/mock/auth/forgot-password" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "doctor@setu.test"
  }'
```

**Response (200 OK)**
```json
{
  "success": true,
  "message": "Password reset link sent to your email. Check your inbox."
}
```

---

### 4. Get Current User Profile

**curl**
```bash
curl -X GET "http://localhost:8000/mock/users/me" \
  -H "Accept: application/json"
```

**Response (200 OK)**
```json
{
  "id": "u_124",
  "full_name": "Dr. Asha Patel",
  "member_id": "D0024",
  "email": "asha@setu.test",
  "mobile": "9876543210",
  "photo_url": "https://api.example.com/photos/asha.jpg",
  "role": "doctor"
}
```

---

### 5. Update User Profile

**curl**
```bash
curl -X PATCH "http://localhost:8000/mock/users/me" \
  -H "Content-Type: application/json" \
  -d '{
    "mobile": "9999999999",
    "photo_url": "https://example.com/new-photo.jpg"
  }'
```

**Response (200 OK)**
```json
{
  "success": true,
  "user": {
    "id": "u_124",
    "full_name": "Dr. Asha Patel",
    "member_id": "D0024",
    "email": "asha@setu.test",
    "mobile": "9999999999",
    "photo_url": "https://example.com/new-photo.jpg",
    "role": "doctor"
  }
}
```

---

## Patient APIs

### 1. Create Patient

**curl**
```bash
curl -X POST "http://localhost:8000/mock/patients" \
  -H "Content-Type: application/json" \
  -d '{
    "full_name": "Rajesh Singh",
    "gender": "Male",
    "date_of_birth": "1988-03-20",
    "age": 35,
    "mobile_number": "+919876543201",
    "address": "456 Park Lane, Mumbai",
    "photo_url": "https://example.com/patient.jpg",
    "created_by": 1,
    "updated_by": 1
  }'
```

**Response (201 Created)**
```json
{
  "patient_id": 3,
  "full_name": "Rajesh Singh",
  "gender": "Male",
  "date_of_birth": "1988-03-20",
  "age": 35,
  "mobile_number": "+919876543201",
  "address": "456 Park Lane, Mumbai",
  "photo_url": "https://example.com/patient.jpg",
  "created_by": 1,
  "updated_by": 1,
  "created_at": "2026-03-25T10:30:00",
  "updated_at": "2026-03-25T10:30:00"
}
```

---

### 2. Get All Patients

**curl**
```bash
curl -X GET "http://localhost:8000/mock/patients?skip=0&limit=10" \
  -H "Accept: application/json"
```

**Response (200 OK)**
```json
[
  {
    "patient_id": 1,
    "full_name": "John Doe",
    "gender": "Male",
    "date_of_birth": "1990-01-15",
    "age": 33,
    "mobile_number": "+1234567890",
    "address": "123 Main St",
    "photo_url": "https://example.com/photo.jpg",
    "created_by": 1,
    "updated_by": 1,
    "created_at": "2024-06-01T12:00:00",
    "updated_at": "2024-06-01T12:00:00"
  },
  {
    "patient_id": 2,
    "full_name": "Dharamshinhbhai Prajapati",
    "gender": "Male",
    "age": 58,
    "mobile_number": "+9876543210",
    "address": "Ramagri Village",
    "created_at": "2024-06-02T09:30:00",
    "updated_at": "2024-06-02T09:30:00"
  }
]
```

---

### 3. Get Patient by ID

**curl**
```bash
curl -X GET "http://localhost:8000/mock/patients/1" \
  -H "Accept: application/json"
```

**Response (200 OK)**
```json
{
  "patient_id": 1,
  "full_name": "John Doe",
  "gender": "Male",
  "date_of_birth": "1990-01-15",
  "age": 33,
  "mobile_number": "+1234567890",
  "address": "123 Main St",
  "photo_url": "https://example.com/photo.jpg",
  "created_by": 1,
  "updated_by": 1,
  "created_at": "2024-06-01T12:00:00",
  "updated_at": "2024-06-01T12:00:00"
}
```

---

### 4. Update Patient

**curl**
```bash
curl -X PUT "http://localhost:8000/mock/patients/1" \
  -H "Content-Type: application/json" \
  -d '{
    "full_name": "John Smith",
    "mobile_number": "+1111111111",
    "age": 34,
    "updated_by": 2
  }'
```

**Response (200 OK)**
```json
{
  "patient_id": 1,
  "full_name": "John Smith",
  "gender": "Male",
  "date_of_birth": "1990-01-15",
  "age": 34,
  "mobile_number": "+1111111111",
  "address": "123 Main St",
  "photo_url": "https://example.com/photo.jpg",
  "created_by": 1,
  "updated_by": 2,
  "created_at": "2024-06-01T12:00:00",
  "updated_at": "2026-03-25T11:15:30"
}
```

---

### 5. Delete Patient

**curl**
```bash
curl -X DELETE "http://localhost:8000/mock/patients/1"
```

**Response (204 No Content)**
```
(empty response)
```

---

### 6. Search Patients

**curl**
```bash
curl -X GET "http://localhost:8000/mock/patients/search/John" \
  -H "Accept: application/json"
```

**curl - by mobile**
```bash
curl -X GET "http://localhost:8000/mock/patients/search/9876543210" \
  -H "Accept: application/json"
```

**Response (200 OK)**
```json
[
  {
    "patient_id": 1,
    "full_name": "John Doe",
    "gender": "Male",
    "date_of_birth": "1990-01-15",
    "age": 33,
    "mobile_number": "+1234567890",
    "address": "123 Main St",
    "photo_url": "https://example.com/photo.jpg",
    "created_by": 1,
    "updated_by": 1,
    "created_at": "2024-06-01T12:00:00",
    "updated_at": "2024-06-01T12:00:00"
  }
]
```

---

## OPD Session APIs

### 1. Start OPD Session

**curl**
```bash
curl -X POST "http://localhost:8000/mock/opd/sessions" \
  -H "Content-Type: application/json" \
  -d '{
    "opd_id": "OPD-RAMAGRI-250322",
    "pin": "123456",
    "village": "Ramagri",
    "desk_role": "registration",
    "created_by": "u_124"
  }'
```

**Response (201 Created)**
```json
{
  "success": true,
  "opd_id": "OPD-RAMAGRI-250322",
  "pin": "123456"
}
```

---

### 2. Join OPD by PIN

**curl**
```bash
curl -X GET "http://localhost:8000/mock/opd/sessions/123456" \
  -H "Accept: application/json"
```

**Response (200 OK)**
```json
{
  "opd_id": "OPD-RAMAGRI-250322",
  "pin": "123456",
  "village": "Ramagri",
  "desk_role": "registration",
  "status": "active",
  "patients": [
    {
      "id": "P1234",
      "name": "Dharamshinhbhai Prajapati",
      "gender": "Male",
      "age": 58,
      "token": 1,
      "status": "waiting",
      "notes": null
    }
  ],
  "created_at": "2026-03-25T10:00:00"
}
```

---

### 3. Add Patient to OPD Session

**curl**
```bash
curl -X POST "http://localhost:8000/mock/opd/sessions/123456/patients" \
  -H "Content-Type: application/json" \
  -d '{
    "id": "P1235",
    "name": "Priya Sharma",
    "gender": "Female",
    "age": 45,
    "token": 2
  }'
```

**Response (201 Created)**
```json
{
  "success": true
}
```

---

### 4. Get OPD Statistics

**curl**
```bash
curl -X GET "http://localhost:8000/mock/opd/stats" \
  -H "Accept: application/json"
```

**Response (200 OK)**
```json
{
  "totalOPDs": 3,
  "vitalsRecorded": 5,
  "consultsDone": 4,
  "medicinesGiven": 3
}
```

---

### 5. Update OPD Patient Status

**curl**
```bash
curl -X PATCH "http://localhost:8000/mock/opd/sessions/123456/patients/P1234" \
  -H "Content-Type: application/json" \
  -d '{
    "status": "consulted",
    "notes": "Complete blood test required"
  }'
```

**Response (200 OK)**
```json
{
  "success": true,
  "patient": {
    "id": "P1234",
    "name": "Dharamshinhbhai Prajapati",
    "gender": "Male",
    "age": 58,
    "token": 1,
    "status": "consulted",
    "notes": "Complete blood test required"
  }
}
```

---

## Clinical APIs

### 1. Record Vitals

**curl**
```bash
curl -X POST "http://localhost:8000/mock/patients/1/vitals" \
  -H "Content-Type: application/json" \
  -d '{
    "temp": "98.6",
    "pulse": "88",
    "bp": "130/85",
    "spo2": "98",
    "blood_sugar": "110",
    "allergies": "Pollen allergy",
    "notes": "Patient has mild fever"
  }'
```

**Response (201 Created)**
```json
{
  "success": true,
  "vitals_id": 501
}
```

---

### 2. Record Consultation

**curl**
```bash
curl -X POST "http://localhost:8000/mock/patients/1/consult" \
  -H "Content-Type: application/json" \
  -d '{
    "diagnosis": ["Hypertension", "Diabetes Type 2"],
    "lab_tests": ["CBC", "FBS", "Cholesterol"],
    "follow_up": "After 2 weeks",
    "doctor_notes": "Monitor BP regularly, reduce salt intake"
  }'
```

**Response (201 Created)**
```json
{
  "success": true,
  "consult_id": 7001
}
```

---

### 3. Dispense Medicines

**curl**
```bash
curl -X POST "http://localhost:8000/mock/patients/1/medicines" \
  -H "Content-Type: application/json" \
  -d '{
    "medicines": [
      {
        "id": "6.2",
        "name": "Aspirin",
        "dosage": "1-0-1",
        "days": 7,
        "timing": "After Meal"
      },
      {
        "id": "8.5",
        "name": "Metformin",
        "dosage": "0-1-1",
        "days": 30,
        "timing": "Before Meal"
      }
    ]
  }'
```

**Response (201 Created)**
```json
{
  "success": true,
  "dispense_id": 9001
}
```

---

### 4. Get Patient History

**curl**
```bash
curl -X GET "http://localhost:8000/mock/patients/1/history" \
  -H "Accept: application/json"
```

**Response (200 OK)**
```json
[
  {
    "id": "vh-1",
    "date": "2026-03-10",
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
```

---

## Health Check

**curl**
```bash
curl -X GET "http://localhost:8000/mock/health" \
  -H "Accept: application/json"
```

**Response (200 OK)**
```json
{
  "status": "healthy",
  "service": "mock-api",
  "timestamp": "2026-03-25T12:30:45.123456"
}
```

---

## Postman Collection Setup

### Step 1: Create Collection
1. Open Postman
2. Click **Collections** → **New Collection**
3. Name it: `SETU Mock API`

### Step 2: Set Variables
Collection Variables:
```
BASE_URL    = http://localhost:8000/mock
PATIENT_ID  = 1
PIN         = 123456
PATIENT_PIN = P1234
```

### Step 3: Add Requests
Create folders:
- `Auth`
- `Patients`
- `OPD Sessions`
- `Clinical`

### Step 4: Use Variables
In each request URL:
```
{{BASE_URL}}/auth/login
{{BASE_URL}}/patients/{{PATIENT_ID}}
{{BASE_URL}}/opd/sessions/{{PIN}}/patients/{{PATIENT_PIN}}
```

### Step 5: Test Requests
Each request can have pre-request scripts and tests:

**Pre-request Script** (save variables):
```javascript
pm.globals.set("PATIENT_ID", 1);
pm.globals.set("PIN", "123456");
```

**Test** (verify response):
```javascript
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});

pm.test("Response contains success", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData.success).to.equal(true);
});
```

### Step 6: Export and Share
- Right-click collection → **Export**
- Save as `.json`
- Share with team

---

## Common Test Scenarios

### Scenario 1: Complete Patient Registration Flow
```bash
# 1. Login
RESPONSE=$(curl -s -X POST "http://localhost:8000/mock/auth/login" \
  -H "Content-Type: application/json" \
  -d '{"email":"doctor@setu.test","password":"secret123"}')

# 2. Create patient
curl -X POST "http://localhost:8000/mock/patients" \
  -H "Content-Type: application/json" \
  -d '{
    "full_name":"New Patient",
    "age":45,
    "mobile_number":"+919999999999",
    "created_by":1,
    "updated_by":1
  }'

# 3. Start OPD
curl -X POST "http://localhost:8000/mock/opd/sessions" \
  -H "Content-Type: application/json" \
  -d '{
    "opd_id":"OPD-TEST-250326",
    "pin":"999999",
    "village":"Test Village",
    "desk_role":"registration",
    "created_by":"u_124"
  }'
```

### Scenario 2: Patient Consultation Workflow
```bash
# 1. Record vitals
curl -X POST "http://localhost:8000/mock/patients/1/vitals" \
  -H "Content-Type: application/json" \
  -d '{"temp":"98.6","pulse":"80","bp":"120/80","spo2":"98"}'

# 2. Record consultation
curl -X POST "http://localhost:8000/mock/patients/1/consult" \
  -H "Content-Type: application/json" \
  -d '{
    "diagnosis":["Hypertension"],
    "lab_tests":["CBC"],
    "follow_up":"1 week",
    "doctor_notes":"Monitor BP"
  }'

# 3. Dispense medicines
curl -X POST "http://localhost:8000/mock/patients/1/medicines" \
  -H "Content-Type: application/json" \
  -d '{
    "medicines":[{
      "id":"1.0",
      "name":"Medicine",
      "dosage":"1-0-1",
      "days":7,
      "timing":"After Meal"
    }]
  }'
```

---

## Error Handling Examples

### Request validation error (400)
```bash
curl -X POST "http://localhost:8000/mock/auth/login" \
  -H "Content-Type: application/json" \
  -d '{"email":"invalid"}'  # Missing password
```

Response:
```json
{
  "detail": [
    {
      "loc": ["body", "password"],
      "msg": "field required",
      "type": "value_error.missing"
    }
  ]
}
```

### Resource not found (404)
```bash
curl -X GET "http://localhost:8000/mock/patients/99999"
```

Response:
```json
{
  "detail": "Patient with ID 99999 not found"
}
```

### Unauthorized (401)
```bash
curl -X POST "http://localhost:8000/mock/auth/login" \
  -H "Content-Type: application/json" \
  -d '{"email":"wrong@test.com","password":"wrong"}'
```

Response:
```json
{
  "detail": "Invalid email or password"
}
```

---

## Performance Testing

**Load test with Apache Bench**
```bash
ab -n 1000 -c 10 http://localhost:8000/mock/health
```

**Load test with wrk**
```bash
wrk -t4 -c100 -d30s http://localhost:8000/mock/health
```

**Slow test with curl**
```bash
curl -w "\nTime taken: %{time_total}s\n" \
  http://localhost:8000/mock/patients
```

---

## Next Steps

1. ✅ Copy curl commands to automate API testing
2. ✅ Import examples into Postman
3. ✅ Integrate with frontend application
4. ✅ Test edge cases and error handling
5. ✅ Load test before production deployment

**Happy testing!** 🚀
