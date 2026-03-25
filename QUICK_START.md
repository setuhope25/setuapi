# SETU Mock API - Quick Start

Get started in 2 minutes! ⚡

---

## 🚀 Fastest Way to Get Running

### 1. Install & Run
```bash
cd /path/to/setuapi
pip install -r requirements.txt
uvicorn main:app --reload
```

**Done!** Access at `http://localhost:8000` ✅

---

## 🔗 Key URLs

| Purpose | URL |
|---------|-----|
| **API Base** | `http://localhost:8000/mock` |
| **Interactive Docs** | `http://localhost:8000/docs` |
| **ReDoc** | `http://localhost:8000/redoc` |
| **Health Check** | `http://localhost:8000/mock/health` |

---

## 📝 Quick API Tests

### Test 1: Login
```bash
curl -X POST "http://localhost:8000/mock/auth/login" \
  -H "Content-Type: application/json" \
  -d '{"email":"doctor@setu.test","password":"secret123"}'
```

### Test 2: Get All Patients
```bash
curl "http://localhost:8000/mock/patients"
```

### Test 3: Create Patient
```bash
curl -X POST "http://localhost:8000/mock/patients" \
  -H "Content-Type: application/json" \
  -d '{
    "full_name":"Test Patient",
    "age":30,
    "mobile_number":"+1234567890",
    "created_by":1,"updated_by":1
  }'
```

---

## 📊 What's Included

| Feature | Status |
|---------|--------|
| ✅ 5 Auth endpoints | Ready |
| ✅ 6 Patient endpoints | Ready |
| ✅ 5 OPD endpoints | Ready |
| ✅ 4 Clinical endpoints | Ready |
| ✅ CORS enabled | Ready |
| ✅ In-memory storage | Ready |
| ✅ Logging | Ready |

**Total: 20+ fully functional mock endpoints**

---

## 🐳 Using Docker?

```bash
# Build and run
docker-compose up --build

# Services started:
# - API: http://localhost:8000
# - Database: localhost:5432
# - pgAdmin: http://localhost:5050
```

---

## 📚 Need More Info?

- **Full Guide**: Read [MOCK_API_GUIDE.md](MOCK_API_GUIDE.md)
- **API Examples**: See [MOCK_API_EXAMPLES.md](MOCK_API_EXAMPLES.md)
- **Deployment**: Check [DEPLOYMENT.md](DEPLOYMENT.md)
- **Original Structure**: View [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md)

---

## 🔑 Default Test Credentials

```
Email:    doctor@setu.test
Password: secret123
Role:     doctor
```

---

## 📦 What Changed?

```
✨ NEW FILES:
  - setumock.py                (all mock endpoints)
  - vercel.json               (serverless config)
  - Dockerfile                (containerization)
  - docker-compose.yml        (full stack)
  - .env.example              (config template)
  - MOCK_API_GUIDE.md         (comprehensive guide)
  - MOCK_API_EXAMPLES.md      (curl/postman examples)
  - DEPLOYMENT.md             (deployment guide)

📝 UPDATED FILES:
  - main.py                   (added CORS, mock router)

✅ UNCHANGED:
  - routers/patients.py
  - database.py
  - schemas.py
  - crud_patient.py
  - All existing functionality preserved!
```

---

## ⚡ Next Steps

1. **Run**: `uvicorn main:app --reload`
2. **Test**: Access `http://localhost:8000/docs`
3. **Integrate**: Use endpoints in frontend
4. **Deploy**: See [DEPLOYMENT.md](DEPLOYMENT.md) for production

---

## 🎯 Pro Tips

- **All endpoints prefixed with `/mock`** - Real endpoints work unchanged
- **Data persists during runtime** - Resets on server restart
- **Interactive docs auto-updating** - `/docs` shows all endpoints
- **Full logging** - Check logs for debugging
- **Production-ready structure** - Easy to migrate to PostgreSQL

---

## 🆘 Stuck?

Check the logs:
```bash
# See what's happening
# Look for INFO/DEBUG messages in terminal

# Or enable debug mode:
# Edit main.py and set DEBUG=True
```

---

## 🚀 Ready to Deploy?

Choose your platform:

- **Vercel** (Recommended): See [DEPLOYMENT.md](DEPLOYMENT.md#vercel-recommended)
- **Docker**: `docker-compose up`
- **Railway**: See [DEPLOYMENT.md](DEPLOYMENT.md#railway)
- **Render**: See [DEPLOYMENT.md](DEPLOYMENT.md#render)
- **AWS**: See [DEPLOYMENT.md](DEPLOYMENT.md#aws)

---

**Happy building! 🎉**

Questions? Check the guides above or review the code comments in `setumock.py`.
