import os
from datetime import datetime
import psycopg2
from psycopg2 import pool, Error
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String, Date, DateTime, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

# ============================================================================
# Neon PostgreSQL Configuration - Read from environment variables
# ============================================================================
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "setu_db")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_PORT = os.getenv("DB_PORT", "5432")

# ============================================================================
# psycopg2 Connection Pool for direct database access
# ============================================================================
try:
    connection_pool = pool.SimpleConnectionPool(
        1,  # minconn - minimum connections
        5,  # maxconn - maximum connections
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT,
        sslmode="require",  # Enforce SSL connection
        connect_timeout=10,
        application_name="setu_api"
    )
except Error as e:
    print(f"Error creating connection pool: {e}")
    connection_pool = None


def get_psycopg2_connection():
    """
    Get a direct psycopg2 connection from the pool.
    Should be closed with close_psycopg2_connection() after use.
    """
    if connection_pool is None:
        raise Error("Connection pool not initialized")
    return connection_pool.getconn()


def close_psycopg2_connection(conn):
    """Return a psycopg2 connection back to the pool"""
    if connection_pool is not None and conn is not None:
        connection_pool.putconn(conn)


def test_database_connection():
    """
    Test database connectivity.
    Returns: (bool, str) - (success, message)
    """
    conn = None
    try:
        conn = get_psycopg2_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        cursor.close()
        return True, "Successfully connected to Neon PostgreSQL"
    except Error as e:
        return False, f"Database connection failed: {str(e)}"
    finally:
        if conn is not None:
            close_psycopg2_connection(conn)


# ============================================================================
# SQLAlchemy Configuration (for backward compatibility with existing CRUD)
# ============================================================================
DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?sslmode=require"

engine = create_engine(
    DATABASE_URL,
    pool_size=5,
    max_overflow=10,
    pool_pre_ping=True,
    pool_recycle=3600,
    connect_args={
        "connect_timeout": 10,
        "application_name": "setu_api"
    }
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# ============================================================================
# SQLAlchemy ORM Models
# ============================================================================
class Patient(Base):
    __tablename__ = "patient"

    patient_id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(255), nullable=False)
    gender = Column(String(50))
    date_of_birth = Column(Date)
    age = Column(Integer)
    mobile_number = Column(String(20))
    address = Column(Text)
    photo_url = Column(String(500))
    created_by = Column(Integer, nullable=False)
    updated_by = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


# ============================================================================
# Database Initialization and Session Management
# ============================================================================
def init_db():
    """Initialize database - creates all tables"""
    Base.metadata.create_all(bind=engine)


def get_db():
    """Dependency to get SQLAlchemy database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

