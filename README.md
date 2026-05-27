# 🏥 Hospital Management System

A simple Hospital Management System built using **MySQL** and **Python**.
Built as a portfolio project to demonstrate SQL and Python skills.

## 📌 Features
- Add and view patients
- View doctors and departments
- Book and manage appointments
- Search patients by name
- Update appointment status
- Prescription tracking

## 🛠️ Tech Stack
- **Database:** MySQL
- **Language:** Python 3
- **Library:** mysql-connector-python

## 🗄️ Database Schema
- `departments` — hospital departments
- `doctors` — doctor details linked to departments
- `patients` — patient records
- `appointments` — links patients and doctors
- `prescriptions` — medicines per appointment

## ⚙️ How to Run

### 1. Clone the repository
```bash
git clone https://github.com/Monish102006/hospital-management-system.git
cd hospital-management-system
```

### 2. Set up the database
- Open MySQL Workbench
- Run `schema.sql` to create all tables
- Run `sample_data.sql` to insert sample data

### 3. Install Python dependency
```bash
pip install mysql-connector-python
```

### 4. Configure database credentials
Open `main.py` and update the connection details:
```python
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="YOUR_MYSQL_PASSWORD",  # ← replace with your password
        database="hospital_db"
    )
```
> ⚠️ Never share or commit your actual password to GitHub!

### 5. Run the app
```bash
python main.py
```

## 📷 Screenshots
![ER-Diagram in WorkBench]("ER.png")

![CLI]("CLI.png")

## 👨‍💻 Author
Monish — [GitHub Profile](https://github.com/Monish102006)