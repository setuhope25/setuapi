-- SQL script to create the patient table in PostgreSQL
-- Run this script in your PostgreSQL database before using the API

CREATE TABLE IF NOT EXISTS patient (
    patient_id SERIAL PRIMARY KEY,
    full_name VARCHAR(255) NOT NULL,
    gender VARCHAR(50),
    date_of_birth DATE,
    age INTEGER,
    mobile_number VARCHAR(20),
    address TEXT,
    photo_url VARCHAR(500),
    created_by INTEGER NOT NULL,
    updated_by INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes for better query performance
CREATE INDEX IF NOT EXISTS idx_patient_full_name ON patient(full_name);
CREATE INDEX IF NOT EXISTS idx_patient_mobile_number ON patient(mobile_number);
CREATE INDEX IF NOT EXISTS idx_patient_created_at ON patient(created_at);

-- Note: The created_by and updated_by columns reference a user table
-- If you have a user table, add foreign key constraints like this:
-- ALTER TABLE patient ADD CONSTRAINT fk_created_by FOREIGN KEY (created_by) REFERENCES user(user_id);
-- ALTER TABLE patient ADD CONSTRAINT fk_updated_by FOREIGN KEY (updated_by) REFERENCES user(user_id);

