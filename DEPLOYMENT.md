# SETU API - Deployment Guide

Complete guide for deploying the SETU API with mock endpoints to various platforms.

---

## Table of Contents
1. [Local Development](#local-development)
2. [Vercel (Recommended)](#vercel-recommended)
3. [Docker](#docker)
4. [Railway](#railway)
5. [Render](#render)
6. [AWS](#aws)
7. [Production Checklist](#production-checklist)

---

## Local Development

### Prerequisites
- Python 3.8+
- pip or conda
- Git

### Setup

1. **Clone Repository**
   ```bash
   git clone https://github.com/your-repo/setuapi.git
   cd setuapi
   ```

2. **Create Virtual Environment**
   ```bash
   # Using venv
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows
   
   # Or using conda
   conda create -n setuapi python=3.11
   conda activate setuapi
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment**
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

5. **Run Server**
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

6. **Access**
   - API: http://localhost:8000
   - Docs: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc
   - Mock Health: http://localhost:8000/mock/health

---

## Vercel (Recommended)

### Why Vercel?
- ✅ Free tier (10GB/month)
- ✅ Automatic HTTPS
- ✅ Global CDN
- ✅ Environment variables management
- ✅ GitHub integration
- ✅ Zero-config deployment

### Step-by-Step Deployment

#### 1. Prepare GitHub Repository
```bash
git init
git add .
git commit -m "Initial commit with mock API"
git branch -M main
git remote add origin https://github.com/your-username/setuapi.git
git push -u origin main
```

#### 2. Create Vercel Account
- Visit https://vercel.com
- Sign up with GitHub
- Authorize Vercel to access repositories

#### 3. Deploy Project

**Option A: CLI (Fastest)**
```bash
# Install Vercel CLI
npm install -g vercel

# Login to Vercel
vercel login

# Deploy
cd /path/to/setuapi
vercel
```

Follow prompts:
```
? Set up and deploy "~/setuapi"? [Y/n] y
? Which scope do you want to deploy to? [your-username]
? Link to existing project? [y/N] n
? What's your project's name? setuapi
? In which directory is your code located? ./
? Want to modify these settings? [y/N] n
```

**Option B: GitHub Integration**
1. Go to https://vercel.com/new
2. Import your GitHub repository
3. Click "Import"
4. Configure settings (should auto-detect):
   - Framework: Other
   - Build Command: `pip install -r requirements.txt`
   - Output Directory: (leave empty)
   - Root Directory: ./
5. Add environment variables (optional)
6. Click "Deploy"

#### 4. Environment Variables
In Vercel Dashboard → Settings → Environment Variables:

```
DATABASE_URL=postgresql://...
DEBUG=False
ENVIRONMENT=production
```

#### 5. Verify Deployment
```bash
# Your API is now live at
https://setuapi.vercel.app

# Test it
curl https://setuapi.vercel.app/mock/health

# Access documentation
https://setuapi.vercel.app/docs
```

#### 6. Custom Domain (Optional)
1. Go to Vercel Dashboard → Project Settings → Domains
2. Add your custom domain
3. Update DNS records as instructed
4. Vercel automatically provisions SSL

#### 7. View Logs
```bash
# Real-time logs
vercel logs

# Function logs
vercel logs --follow
```

#### 8. Redeploy
```bash
# Automatic: Push to main branch
git push origin main

# Manual
vercel --prod
```

---

## Docker

### Build Image

```bash
# Build
docker build -t setuapi:latest .

# Run
docker run -p 8000:8000 setuapi:latest

# With environment variables
docker run -p 8000:8000 \
  -e DATABASE_URL=postgresql://user:pass@host:5432/db \
  setuapi:latest

# With volume mount
docker run -p 8000:8000 \
  -v /path/to/data:/app/data \
  setuapi:latest
```

### Docker Compose (Full Stack)

```bash
# Start all services
docker-compose up --build

# Run in background
docker-compose up -d

# View logs
docker-compose logs -f api

# Stop services
docker-compose down

# Stop and remove volumes
docker-compose down -v
```

### Services
```
API          → http://localhost:8000
Database     → localhost:5432
pgAdmin      → http://localhost:5050
```

### Push to Docker Hub

```bash
# Login
docker login

# Tag image
docker tag setuapi:latest your-username/setuapi:latest

# Push
docker push your-username/setuapi:latest

# Pull and run
docker run -p 8000:8000 your-username/setuapi:latest
```

---

## Railway

### Deployment Steps

1. **Connect GitHub**
   - Visit https://railway.app
   - Sign up with GitHub
   - Authorize Railway

2. **Create Project**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository

3. **Configure Service**
   - Railway should auto-detect Python
   - Add environment variables if needed:
     ```
     DATABASE_URL=
     DEBUG=False
     ENVIRONMENT=production
     ```

4. **Deploy**
   - Click "Deploy"
   - Wait for build to complete (~2-3 minutes)

5. **Access**
   ```
   https://setuapi-prod.up.railway.app
   ```

6. **Database (Optional)**
   - Add PostgreSQL plugin from Railway dashboard
   - Railway auto-creates `DATABASE_URL`

### Railway Advantages
- ✅ Generous free tier
- ✅ Built-in database options
- ✅ Automatic SSL
- ✅ Easy variable management

---

## Render

### Deployment Steps

1. **Create Account**
   - Visit https://render.com
   - Sign up with GitHub
   - Connect repository

2. **Create Web Service**
   - Click "New" → "Web Service"
   - Select your repository
   - Configure:
     ```
     Name:  setuapi
     Environment: Python 3
     Build Command: pip install -r requirements.txt
     Start Command: uvicorn main:app --host 0.0.0.0 --port 8000
     ```

3. **Environment Variables**
   - Add under Environment:
     ```
     PYTHON_VERSION=3.11
     DEBUG=False
     ```

4. **Deploy**
   - Click "Create Web Service"
   - Wait for deployment (~3-5 minutes)

5. **Access**
   - Your app: `https://setuapi.onrender.com`
   - Docs: `https://setuapi.onrender.com/docs`

### Keep Service Running (Free Tier)
```bash
# Render spins down free tier after 15 min inactivity
# To keep alive, add uptime monitor:
# Use Uptime Robot (https://uptimerobot.com)
# Set to ping your API every 10 minutes
```

---

## AWS

### Option 1: AWS EC2 (Simple)

1. **Launch EC2 Instance**
   - AMI: Ubuntu 22.04 LTS
   - Instance: t3.micro (free tier eligible)
   - Security Group: Allow HTTP (80), HTTPS (443), SSH (22)

2. **SSH Connect**
   ```bash
   ssh -i your-key.pem ubuntu@your-instance-ip
   ```

3. **Setup Application**
   ```bash
   # Update system
   sudo apt update && sudo apt upgrade -y
   
   # Install Python and dependencies
   sudo apt install python3-pip python3-venv -y
   
   # Clone repository
   git clone https://github.com/your-repo/setuapi.git
   cd setuapi
   
   # Create virtual environment
   python3 -m venv venv
   source venv/bin/activate
   
   # Install dependencies
   pip install -r requirements.txt
   ```

4. **Configure Systemd Service**
   ```bash
   sudo nano /etc/systemd/system/setuapi.service
   ```
   
   Content:
   ```ini
   [Unit]
   Description=SETU API
   After=network.target
   
   [Service]
   User=ubuntu
   WorkingDirectory=/home/ubuntu/setuapi
   ExecStart=/home/ubuntu/setuapi/venv/bin/uvicorn main:app --host 0.0.0.0 --port 8000
   Restart=always
   RestartSec=10
   
   [Install]
   WantedBy=multi-user.target
   ```
   
   ```bash
   # Enable and start service
   sudo systemctl enable setuapi
   sudo systemctl start setuapi
   sudo systemctl status setuapi
   ```

5. **Setup Nginx Reverse Proxy**
   ```bash
   sudo apt install nginx -y
   sudo nano /etc/nginx/sites-available/setuapi
   ```
   
   Content:
   ```nginx
   server {
       listen 80;
       server_name your-domain.com;
       
       location / {
           proxy_pass http://127.0.0.1:8000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }
   }
   ```
   
   ```bash
   sudo ln -s /etc/nginx/sites-available/setuapi /etc/nginx/sites-enabled/
   sudo systemctl restart nginx
   ```

6. **Add SSL (Let's Encrypt)**
   ```bash
   sudo apt install certbot python3-certbot-nginx -y
   sudo certbot --nginx -d your-domain.com
   ```

### Option 2: AWS Lambda + API Gateway

Benefits:
- ✅ Truly serverless
- ✅ Pay only for requests
- ✅ Auto-scaling
- ✅ Lower costs for low traffic

**Using Serverless Framework:**
```bash
npm install -g serverless

# Create project
serverless create --template aws-python-fastapi

# Configure AWS credentials
aws configure

# Deploy
serverless deploy
```

---

## Production Checklist

Before deploying to production:

### Code Quality
- [ ] All endpoints tested
- [ ] Error handling implemented
- [ ] CORS configured correctly
- [ ] Logging implemented
- [ ] No hardcoded secrets/credentials
- [ ] Code review completed

### Configuration
- [ ] `.env` not committed to git
- [ ] `.env.example` has all required variables
- [ ] **DEBUG=False** in production
- [ ] Proper log levels set
- [ ] Database connection string valid

### Security
- [ ] HTTPS enabled
- [ ] CORS origins restricted
- [ ] Input validation on all endpoints
- [ ] No sensitive data in logs
- [ ] Rate limiting implemented (optional)
- [ ] Secrets stored in environment variables

### Performance
- [ ] Load tested
- [ ] Database indexes created
- [ ] Cache strategy implemented (if needed)
- [ ] CDN configured (if needed)

### Monitoring
- [ ] Error tracking setup (Sentry, etc.)
- [ ] Health checks configured
- [ ] Uptime monitoring active
- [ ] Logs aggregation setup
- [ ] Alerting configured

### Documentation
- [ ] API documentation complete
- [ ] Deployment guide written
- [ ] Environment variables documented
- [ ] Troubleshooting guide created

---

## Monitoring & Maintenance

### Health Checks
```bash
# Monitor API health
curl -X GET "https://setuapi.vercel.app/mock/health"

# Monitor with watch
watch -n 5 'curl -s https://setuapi.vercel.app/mock/health | jq'
```

### View Logs

**Vercel:**
```bash
vercel logs --follow
```

**Docker:**
```bash
docker-compose logs -f api
```

**Railway/Render:**
- View in dashboard

### Update Deployment

**After code changes:**
```bash
# Commit and push to main
git add .
git commit -m "feature: update endpoints"
git push origin main

# Vercel/Railway/Render auto-redeploy
# Docker: rebuild and redeploy
```

### Database Backups
```bash
# Export PostgreSQL backup
pg_dump postgresql://user:pass@host:5432/db > backup.sql

# Restore from backup
psql postgresql://user:pass@host:5432/db < backup.sql
```

---

## Troubleshooting

### 502 Bad Gateway on Vercel
```bash
# Check Cypress logs
vercel logs

# Might be Python version issue - verify vercel.json
# Ensure runtime: python3.11
```

### Connection Timeout
```bash
# Check API is running
curl http://localhost:8000/health

# Check port forwarding
lsof -i :8000
```

### Database Connection Failed
```bash
# Verify DATABASE_URL
echo $DATABASE_URL

# Test connection
psql $DATABASE_URL

# Check credentials in .env
cat .env | grep DATABASE
```

### High Memory Usage
```bash
# Monitor
docker stats

# Optimize: Limit container memory
docker run -m 512m setuapi:latest
```

---

## Cost Comparison

| Platform | Tier | Monthly Cost | Suitable For |
|----------|------|------------|--------------|
| Vercel | Free/Pro | $0-20 | Low-medium traffic |
| Railway | Free/Hobby | $0-7 | Low-medium traffic |
| Render | Free | $0 | Very low traffic |
| AWS EC2 | Free/Paid | $0-30 | Medium-high traffic |
| AWS Lambda | Serverless | $0-5 | Highly variable traffic |

---

## Next Steps

1. ✅ Choose platform (Vercel recommended)
2. ✅ Follow deployment steps
3. ✅ Configure environment variables
4. ✅ Set up monitoring
5. ✅ Configure custom domain (optional)
6. ✅ Setup CI/CD pipeline (optional)
7. ✅ Plan database integration

---

## Support

- **FastAPI**: https://fastapi.tiangolo.com
- **Uvicorn**: https://www.uvicorn.org
- **Vercel Docs**: https://vercel.com/docs
- **Docker**: https://docs.docker.com

**Happy deploying!** 🚀
