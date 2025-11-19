from sqlalchemy import create_engine, Column, Integer, String, Date, DateTime, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

# Database URL - update with your PostgreSQL connection string
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://setuapi:SetuHope1979@localhost:5432/setusaathi")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


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


def init_db():
    """Initialize database - creates all tables"""
    Base.metadata.create_all(bind=engine)


def get_db():
    """Dependency to get database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

