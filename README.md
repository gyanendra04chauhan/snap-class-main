# 📸 Smart Attendance System using Face Recognition   
LIVE DEMO= https://snap-class-main-svxzlqzdogu4avuzo4adgh.streamlit.app/

A web-based attendance system that automates classroom attendance using facial recognition. A teacher uploads **one group photograph** of the class, and the system detects, recognizes and marks attendance for every enrolled student in a single step.

---

## 📌 Overview

Attendance in classrooms is still largely manual and roll-call based. It consumes valuable teaching time in every lecture and is vulnerable to human error and **proxy attendance**, where one student marks another as present.

This project replaces that process with an automated, face-recognition-based approach. Teachers and students register **subject-wise** using a unique subject code, log in through a secure role-based system, and attendance is marked automatically from a single classroom photo.

---

## 🎯 Objectives

- Allow teachers and students to register subject-wise, with every subject identified by a unique subject code
- Provide a secure, role-based login system for teachers and students
- Let a teacher mark attendance for the entire class in one step using a single group photograph
- Automatically detect and recognize faces in the photo, marking matched students **Present** and all other enrolled students **Absent**
- Securely store subject-wise attendance records for later viewing and reporting

---

## ✨ Features

- **Subject-wise registration** using unique subject codes
- **Role-based login** for teachers and students
- **One-photo attendance**: upload a single group photo to mark the whole class
- **Automatic Present/Absent marking** for every student enrolled in the subject
- **Secure password storage** using bcrypt hashing (no plain-text credentials)
- **Teacher Dashboard**: registered subjects, classes and attendance reports
- **Student Dashboard**: registered subjects and attendance history
- **QR code generation** for each subject code for quick, error-free enrollment
- **Voice processing** support as an additional, secondary layer of identity verification

---

## 🧩 System Modules

### 1. Registration Module
- **Teachers** register against the subject(s) they teach using the subject's unique code.
- **Students** register against the subject(s) they are enrolled in using the same code, along with a reference photograph that is processed into a facial encoding.
- Passwords are hashed with bcrypt before being stored.

### 2. Login Module
- A common, role-based login screen for both roles.
- Teachers are directed to the **Teacher Dashboard**, students to the **Student Dashboard**.

### 3. Attendance Marking Module
- The teacher opens the relevant subject/class and uploads a group photo taken during the lecture.
- The system detects every face and generates a facial encoding for each.
- Each encoding is compared with the stored encodings of students registered for that subject.
- Matched students are marked **Present**; all other registered students are marked **Absent**.
- The record, with date and time, is saved to the database and can be viewed by the teacher.

---

## 🔄 Workflow

1. Teacher and student both register for a subject using its unique subject code.
2. Both log in with their registered credentials.
3. Teacher opens the subject/class and uploads a group photo of the class.
4. System performs face detection and recognition on the photo.
5. Attendance is auto-marked (Present/Absent) for every registered student and saved to the database.
6. Teacher views the attendance report for that class/subject.

---

## 🛠️ Tech Stack

| Category | Technology | Purpose |
|---|---|---|
| App Framework | Streamlit | Interactive web app and dashboards for teachers and students |
| Backend & Database | Supabase | Stores user profiles, subjects, facial encodings and attendance records |
| Authentication | bcrypt | Hashing and verifying login passwords |
| Data Handling | NumPy, Pandas | Processing facial-encoding arrays and generating attendance reports |
| Face Recognition | scikit-learn, dlib-bin, face_recognition_models | Detecting faces in the classroom photo and matching them with registered students |
| Image Processing | Pillow | Reading and preparing images for the recognition pipeline |
| QR Code | segno | Generating a QR code for each subject code |
| Voice Processing | librosa, resemblyzer | Extracting voice features for secondary identity verification |

**Language:** Python

---

## 🧪 Testing & Validation

- **Unit testing** of Registration and Login (sign-up, subject-code uniqueness, password authentication)
- **Face-recognition testing** under varying classroom lighting, group size and camera angle
- **Threshold tuning** of the face-match confidence to balance false matches (wrong student marked present) against false misses (present student marked absent)
- **Manual cross-verification** of the system output against a manual roll call for sample sessions
- **Multi-subject testing** to confirm students registered in several subjects are marked correctly and independently for each

---

## 📈 Expected Results

- Attendance marked considerably faster than manual roll call, since one photo covers the whole class
- A noticeable reduction in proxy attendance, since presence is verified by face recognition
- Consistent, subject-wise attendance records that can be retrieved at any time
- A working face-match accuracy rate under normal classroom lighting, to be quantified during testing on real classroom photographs

---

## 🚀 Future Scope

- Extend the voice-recognition module for live, real-time attendance instead of a single static photograph
- Automated email/SMS notifications to parents when a student's absences cross a defined threshold
- Analytics dashboard showing attendance trends by student, subject and time period
- Mobile application so teachers can capture and upload the classroom photo directly from their phone

---


---

## 📚 References

- [face_recognition library](https://github.com/ageitgey/face_recognition)
- [dlib C++ Library](http://dlib.net/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Supabase Documentation](https://supabase.com/docs)
- [scikit-learn Documentation](https://scikit-learn.org/)

---

## 📄 License

This project was developed as an academic mini project. Add a license of your choice (e.g., MIT) if you plan to open-source it.
