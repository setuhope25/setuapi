-- =========================
-- VILLAGE
-- =========================
CREATE TABLE village (
  village_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  name VARCHAR(100)
);

INSERT INTO village (name) VALUES
('Village A'),
('Village B');

-- =========================
-- USERS
-- =========================
CREATE TABLE users (
  user_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  firebase_uid VARCHAR(128),
  member_id VARCHAR(50),
  full_name VARCHAR(100),
  phone_number VARCHAR(15),
  date_of_birth DATE,
  age INT,
  age_type VARCHAR(10),
  role VARCHAR(20),
  is_active BOOLEAN DEFAULT TRUE
);

INSERT INTO users (firebase_uid, member_id, full_name, phone_number, age, age_type, role, is_active) VALUES
('uid1','M001','NGO Worker 1','9999999991',30,'approx','ngo_staff',true),
('uid2','D001','Doctor Strange','9999999992',45,'approx','doctor',true);

-- =========================
-- DOCTORS
-- =========================
CREATE TABLE doctors (
  doctor_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  user_id INT REFERENCES users(user_id) ON DELETE CASCADE,
  specialization VARCHAR(100)
);

INSERT INTO doctors (user_id, specialization) VALUES
(2,'General Physician');

-- =========================
-- PATIENTS
-- =========================
CREATE TABLE patients (
  patient_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  full_name VARCHAR(100),
  image_path varchar(100),
  gender boolean, 
 
  date_of_birth DATE,
  age INT,
  age_type VARCHAR(10),
   phone_number VARCHAR(15),
   address varchar(150),
  is_active BOOLEAN DEFAULT TRUE  village_id INT REFERENCES village(village_id)
);

-- insert to be generated  by gpt 

-- =========================
-- OPD (CAMP)
-- =========================
CREATE TABLE opd (
  opd_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  village_id INT REFERENCES village(village_id),
  opd_name VARCHAR(100),
  opd_date DATE,
  created_by INT REFERENCES users(user_id)
);

INSERT INTO opd (village_id, opd_name, opd_date, created_by) VALUES
(1,'OPD Camp 1','2026-03-20',1),
(1,'OPD Camp 2','2026-03-21',1);

-- =========================
-- CASES
-- =========================
CREATE TABLE cases (
  case_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  opd_id INT REFERENCES opd(opd_id),
  patient_id INT REFERENCES patients(patient_id),
  doctor_id INT REFERENCES doctors(doctor_id),
  status VARCHAR(50)
);

INSERT INTO cases (opd_id, patient_id, doctor_id, status) VALUES
(1,1,1,'in_consultation'),
(1,2,1,'waiting'),
(2,1,1,'completed');

-- =========================
-- VITAL TYPES
-- =========================
CREATE TABLE vital_types (
  vital_type_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  name VARCHAR(50),
  unit varchar(50) -- kg, ft , mmh
);

INSERT INTO vital_types (name) VALUES
('Temperature'),
('Blood Pressure');

-- =========================
-- PATIENT VITALS
-- =========================
CREATE TABLE patient_vitals (
  vital_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  case_id INT REFERENCES cases(case_id),
  vital_type_id INT REFERENCES vital_types(vital_type_id),
  value VARCHAR(50)
);

INSERT INTO patient_vitals (case_id, vital_type_id, value) VALUES
(1,1,'101 F'),
(1,2,'120/80');

-- =========================
-- SYMPTOMS
-- =========================
CREATE TABLE symptoms (
  symptom_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  name VARCHAR(100)
);

INSERT INTO symptoms (name) VALUES
('Fever'),
('Cold');

-- =========================
-- CASE SYMPTOMS
-- =========================
CREATE TABLE case_symptoms (
  id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  case_id INT REFERENCES cases(case_id),
  symptom_id INT REFERENCES symptoms(symptom_id)
);

INSERT INTO case_symptoms (case_id, symptom_id) VALUES
(1,1),
(1,2);

-- =========================
-- DIAGNOSIS
-- =========================
CREATE TABLE diagnosis (
  diagnosis_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  name VARCHAR(100)
);

INSERT INTO diagnosis (name) VALUES
('Viral Fever');

-- =========================
-- CASE DIAGNOSIS
-- =========================
CREATE TABLE case_diagnosis (
  id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  case_id INT REFERENCES cases(case_id),
  diagnosis_id INT REFERENCES diagnosis(diagnosis_id)
);

INSERT INTO case_diagnosis (case_id, diagnosis_id) VALUES
(1,1);

-- =========================
-- MEDICINES
-- =========================
CREATE TABLE medicines (
  medicine_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  name VARCHAR(100)
);

INSERT INTO medicines (name) VALUES
('Paracetamol');

-- =========================
-- PRESCRIPTIONS
-- =========================
CREATE TABLE prescriptions (
  prescription_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  case_id INT REFERENCES cases(case_id),
  doctor_id INT REFERENCES doctors(doctor_id)
);

INSERT INTO prescriptions (case_id, doctor_id) VALUES
(1,1);

-- =========================
-- PRESCRIPTION ITEMS
-- =========================
CREATE TABLE prescription_items (
  id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  prescription_id INT REFERENCES prescriptions(prescription_id),
  medicine_id INT REFERENCES medicines(medicine_id),
  dosage VARCHAR(50)
);

INSERT INTO prescription_items (prescription_id, medicine_id, dosage) VALUES
(1,1,'1 tablet twice daily');

-- =========================
-- DISPENSING
-- =========================
CREATE TABLE dispensing (
  dispensing_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  prescription_id INT REFERENCES prescriptions(prescription_id),
  given_by INT REFERENCES users(user_id),
  status VARCHAR(20)
);

INSERT INTO dispensing (prescription_id, given_by, status) VALUES
(1,1,'dispensed');

-- =========================
-- CONSULTATION SESSIONS
-- =========================
CREATE TABLE consultation_sessions (
  session_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  case_id INT REFERENCES cases(case_id),
  doctor_id INT REFERENCES doctors(doctor_id),
  video_link TEXT
);

INSERT INTO consultation_sessions (case_id, doctor_id, video_link) VALUES
(1,1,'https://video-call-link');