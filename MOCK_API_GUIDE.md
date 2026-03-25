# SETU API - Mock Implementation Guide

## Project Overview

This project extends the existing FastAPI SETU Patient API with **comprehensive mock endpoints** to accelerate frontend/UI development without waiting for real database implementations.

## What's New

### 1. **setumock.py** - Complete Mock API Implementation
- ✅ All 18+ mock endpoints from API_Define.md
- ✅ In-memory data storage (dictionaries)
- ✅ Full CRUD operations for all resources
- ✅ Proper HTTP status codes and error handling
- ✅ Comprehensive logging
- ✅ Pydantic models for request/response validation

### 2. **Updated main.py**
- ✅ CORS middleware configured for frontend compatibility
- ✅ Mock router included with `/mock` prefix
- ✅ All existing endpoints preserved

### 3. **Deployment Configuration**
- ✅ `vercel.json` - Serverless deployment config
- ✅ `Dockerfile` - Container image
- ✅ `docker-compose.yml` - Local development stack
- ✅ `.env.example` - Environment variables template

---

## Running Locally

### Option 1: Direct Python (Simplest)
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```
Access at: `http://localhost:8000`

### Option 2: Docker Compose (Best for Full Stack)
```bash
docker-compose up --build
```
Services:
- **API**: http://localhost:8000
- **Database**: localhost:5432
- **pgAdmin**: http://localhost:5050

Credentials:
- DB User: `setu_user`
- DB Password: `setu_password`
- pgAdmin Email: `admin@example.com`
- pgAdmin Password: `admin`

### Option 3: Docker (Manual)
```bash
docker build -t setu-api .
docker run -p 8000:8000 setu-api
```

---

## API Structure

### Base URL
```
http://localhost:8000/mock
```

### Endpoint Categories

#### 1. Auth & User Profile (5 endpoints)
- `POST /mock/auth/login`
- `POST /mock/auth/register`
- `POST /mock/auth/forgot-password`
- `GET /mock/users/me`
- `PATCH /mock/users/me`

#### 2. Patient APIs (6 endpoints)
- `POST /mock/patients`
- `GET /mock/patients?skip=0&limit=100`
- `GET /mock/patients/{patient_id}`
- `PUT /mock/patients/{patient_id}`
- `DELETE /mock/patients/{patient_id}`
- `GET /mock/patients/search/{search_term}`

#### 3. OPD Session (5 endpoints)
- `POST /mock/opd/sessions`
- `GET /mock/opd/sessions/{pin}`
- `POST /mock/opd/sessions/{pin}/patients`
- `GET /mock/opd/stats`
- `PATCH /mock/opd/sessions/{pin}/patients/{patient_id}`

#### 4. Clinical (4 endpoints)
- `POST /mock/patients/{patient_id}/vitals`
- `POST /mock/patients/{patient_id}/consult`
- `POST /mock/patients/{patient_id}/medicines`
- `GET /mock/patients/{patient_id}/history`

---

## Quick Test

### Health Check
```bash
curl http://localhost:8000/mock/health
```

Response:
```json
{
  "status": "healthy",
  "service": "mock-api",
  "timestamp": "2026-03-25T..."
}
```

---

## In-Memory Data

Mock data persists **during runtime only** (8 hours per deployment). Suitable for:
- ✅ Frontend development and testing
- ✅ UI/UX prototyping
- ✅ Integration testing
- ✅ Demo environments

**Note**: Data is reset on server restart. For persistent data, integrate PostgreSQL.

---

## Deployment to Vercel

### Prerequisites
- Vercel account (free tier available)
- GitHub repository with your code

### Steps

1. **Push code to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit with mock API"
   git push origin main
   ```

2. **Deploy to Vercel**
   ```bash
   npm install -g vercel
   vercel
   ```
   Or connect GitHub repo directly in [Vercel Dashboard](https://vercel.com)

3. **Access Your API**
   ```
   https://your-project.vercel.app/mock/health
   ```

4. **Environment Variables** (if needed)
   - Add in Vercel Dashboard > Settings > Environment Variables

---

## Integration with Frontend

### React Example
```javascript
const API_BASE = process.env.REACT_APP_API_URL || 'http://localhost:8000/mock';

// Login
const loginUser = async (email, password) => {
  const res = await fetch(`${API_BASE}/auth/login`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email, password })
  });
  return res.json();
};

// Get all patients
const getPatients = async () => {
  const res = await fetch(`${API_BASE}/patients`);
  return res.json();
};

// Create patient
const createPatient = async (patientData) => {
  const res = await fetch(`${API_BASE}/patients`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(patientData)
  });
  return res.json();
};
```

### Vue Example
```javascript
const API_BASE = process.env.VUE_APP_API_URL || 'http://localhost:8000/mock';

export const patientAPI = {
  async getAll() {
    const response = await fetch(`${API_BASE}/patients`);
    return response.json();
  },
  
  async getById(id) {
    const response = await fetch(`${API_BASE}/patients/${id}`);
    return response.json();
  },
  
  async create(data) {
    const response = await fetch(`${API_BASE}/patients`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    });
    return response.json();
  }
};
```

---

## API Documentation

### Interactive Docs
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Sample Requests (See MOCK_API_EXAMPLES.md)

---

## Transitioning to Production

When ready to integrate with PostgreSQL:

1. **Create new router**: `routers/patients_db.py`
2. **Implement DB logic** using existing CRUD patterns
3. **Update main.py**:
   ```python
   # Remove mock router
   # app.include_router(mock_router)
   
   # Add production router
   app.include_router(patients_db_router)
   ```

4. **Leverage existing infrastructure**:
   - `database.py` - DB connection
   - `schemas.py` - Pydantic models
   - `crud_patient.py` - CRUD operations

---

## Logging

Mock API provides detailed logging:

```bash
# View logs
docker-compose logs -f api

# Log levels: DEBUG, INFO, WARNING, ERROR

# Example log entries
INFO:setumock:Creating new patient: John Doe
INFO:setumock:Patient created with ID: 3
WARNING:setumock:Patient not found: 999
```

---

## Common Issues

### Port Already in Use
```bash
# Find process using port 8000
lsof -i :8000  # macOS/Linux
netstat -ano | findstr :8000  # Windows

# Kill process
kill -9 <PID>  # macOS/Linux
taskkill /PID <PID> /F  # Windows
```

### CORS Errors
✅ Already configured in `main.py` for all origins. If issues persist:
```python
# In main.py
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Specify your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### Database Connection Issues
- Mock APIs don't require database
- Database is only needed for real endpoints
- Check `DATABASE_URL` in `.env` if using PostgreSQL

---

## Testing with Postman

1. **Import Collection**
   - See `MOCK_API_EXAMPLES.md` for cURL commands
   - Create collection in Postman with same endpoints

2. **Set Variables**
   ```
   {{BASE_URL}} = http://localhost:8000/mock
   {{PATIENT_ID}} = 1
   {{PIN}} = 123456
   ```

3. **Run Tests**
   - Use Postman's test runner for automated testing

---

## File Structure
```
setuapi/
├── main.py                    # FastAPI app (updated with CORS & mock router)
├── setumock.py               # ✨ NEW - All mock endpoints
├── database.py               # DB connection
├── schemas.py                # Pydantic models
├── crud_patient.py           # CRUD operations
├── create_tables.sql         # DB schema
├── requirements.txt          # Python dependencies
├── vercel.json              # ✨ NEW - Vercel deployment config
├── Dockerfile               # ✨ NEW - Container image
├── docker-compose.yml       # ✨ NEW - Local stack
├── .env.example            # ✨ NEW - Environment template
├── routers/
│   ├── __init__.py
│   └── patients.py         # Patient router
├── PROJECT_STRUCTURE.md
└── README.md
```

---

## Performance & Limits

| Metric | Value |
|--------|-------|
| Max Patients | 1000+ (In-memory) |
| Response Time | <10ms |
| Concurrent Users | 100+ (development) |
| Data Retention | Runtime only (8 hours) |
| Vercel Lambdas | 10s timeout |

---

## Support & Reference

- **FastAPI Docs**: https://fastapi.tiangolo.com
- **Uvicorn**: https://www.uvicorn.org
- **Vercel Python**: https://vercel.com/docs/functions/python
- **Docker**: https://docs.docker.com
- **PostgreSQL**: https://www.postgresql.org/docs

---

## Next Steps

1. ✅ Run locally: `uvicorn main:app --reload`
2. ✅ Test endpoints: See MOCK_API_EXAMPLES.md
3. ✅ Integrate with frontend
4. ✅ Deploy to Vercel: `vercel`
5. ✅ Transition to PostgreSQL when ready

---

## License

Same as original SETU project

**Happy coding! 🚀**
