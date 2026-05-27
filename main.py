import mysql.connector
import config
from datetime import date

# ─────────────────────────────────────────
#  DATABASE CONNECTION
# ─────────────────────────────────────────
def get_connection():
    return mysql.connector.connect(
        host=config.DB_HOST,
        user=config.DB_USER,
        password=config.DB_PASSWORD,
        database=config.DB_NAME
    )

# ─────────────────────────────────────────
#  1. ADD PATIENT
# ─────────────────────────────────────────
def add_patient():
    print("\n--- Add New Patient ---")
    name        = input("Patient Name   : ")
    age         = input("Age            : ")
    gender      = input("Gender (Male/Female/Other): ")
    phone       = input("Phone          : ")
    blood_group = input("Blood Group    : ")

    conn   = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO patients (name, age, gender, phone, blood_group)
        VALUES (%s, %s, %s, %s, %s)
    """, (name, age, gender, phone, blood_group))
    conn.commit()
    print("✅ Patient added successfully!")
    cursor.close()
    conn.close()

# ─────────────────────────────────────────
#  2. VIEW ALL PATIENTS
# ─────────────────────────────────────────
def view_patients():
    print("\n--- All Patients ---")
    conn   = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT patient_id, name, age, gender, blood_group FROM patients")
    rows = cursor.fetchall()
    print(f"\n{'ID':<5} {'Name':<20} {'Age':<5} {'Gender':<10} {'Blood Group'}")
    print("-" * 50)
    for row in rows:
        print(f"{row[0]:<5} {row[1]:<20} {row[2]:<5} {row[3]:<10} {row[4]}")
    cursor.close()
    conn.close()

# ─────────────────────────────────────────
#  3. VIEW ALL DOCTORS
# ─────────────────────────────────────────
def view_doctors():
    print("\n--- All Doctors ---")
    conn   = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT d.doctor_id, d.name, d.spec, dept.dept_name
        FROM doctors d
        JOIN departments dept ON d.dept_id = dept.dept_id
    """)
    rows = cursor.fetchall()
    print(f"\n{'ID':<5} {'Name':<25} {'Specialization':<25} {'Department'}")
    print("-" * 70)
    for row in rows:
        print(f"{row[0]:<5} {row[1]:<25} {row[2]:<25} {row[3]}")
    cursor.close()
    conn.close()

# ─────────────────────────────────────────
#  4. BOOK APPOINTMENT
# ─────────────────────────────────────────
def book_appointment():
    print("\n--- Book Appointment ---")
    view_patients()
    patient_id = input("\nEnter Patient ID : ")
    view_doctors()
    doctor_id  = input("\nEnter Doctor ID  : ")
    appt_date  = input("Appointment Date (YYYY-MM-DD): ")

    conn   = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO appointments (patient_id, doctor_id, appt_date, status)
        VALUES (%s, %s, %s, 'Scheduled')
    """, (patient_id, doctor_id, appt_date))
    conn.commit()
    print("✅ Appointment booked successfully!")
    cursor.close()
    conn.close()

# ─────────────────────────────────────────
#  5. VIEW ALL APPOINTMENTS
# ─────────────────────────────────────────
def view_appointments():
    print("\n--- All Appointments ---")
    conn   = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT 
            a.appt_id,
            p.name AS patient_name,
            d.name AS doctor_name,
            a.appt_date,
            a.status
        FROM appointments a
        JOIN patients p ON a.patient_id = p.patient_id
        JOIN doctors  d ON a.doctor_id  = d.doctor_id
    """)
    rows = cursor.fetchall()
    print(f"\n{'ID':<5} {'Patient':<20} {'Doctor':<20} {'Date':<15} {'Status'}")
    print("-" * 70)
    for row in rows:
        print(f"{row[0]:<5} {row[1]:<20} {row[2]:<20} {str(row[3]):<15} {row[4]}")
    cursor.close()
    conn.close()

# ─────────────────────────────────────────
#  6. SEARCH PATIENT BY NAME
# ─────────────────────────────────────────
def search_patient():
    print("\n--- Search Patient ---")
    name = input("Enter patient name to search: ")
    conn   = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT patient_id, name, age, gender, phone, blood_group
        FROM patients
        WHERE name LIKE %s
    """, (f"%{name}%",))
    rows = cursor.fetchall()
    if rows:
        print(f"\n{'ID':<5} {'Name':<20} {'Age':<5} {'Gender':<10} {'Phone':<15} {'Blood Group'}")
        print("-" * 65)
        for row in rows:
            print(f"{row[0]:<5} {row[1]:<20} {row[2]:<5} {row[3]:<10} {row[4]:<15} {row[5]}")
    else:
        print("❌ No patient found.")
    cursor.close()
    conn.close()

# ─────────────────────────────────────────
#  7. UPDATE APPOINTMENT STATUS
# ─────────────────────────────────────────
def update_appointment_status():
    print("\n--- Update Appointment Status ---")
    view_appointments()
    appt_id = input("\nEnter Appointment ID to update: ")
    print("1. Scheduled\n2. Completed\n3. Cancelled")
    choice = input("Choose new status (1/2/3): ")
    status_map = {"1": "Scheduled", "2": "Completed", "3": "Cancelled"}
    status = status_map.get(choice)
    if not status:
        print("❌ Invalid choice.")
        return
    conn   = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE appointments SET status = %s WHERE appt_id = %s
    """, (status, appt_id))
    conn.commit()
    print(f"✅ Appointment status updated to '{status}'!")
    cursor.close()
    conn.close()

# ─────────────────────────────────────────
#  MAIN MENU
# ─────────────────────────────────────────
def main():
    while True:
        print("\n" + "="*40)
        print("   🏥 HOSPITAL MANAGEMENT SYSTEM")
        print("="*40)
        print("  1. Add New Patient")
        print("  2. View All Patients")
        print("  3. View All Doctors")
        print("  4. Book Appointment")
        print("  5. View All Appointments")
        print("  6. Search Patient by Name")
        print("  7. Update Appointment Status")
        print("  0. Exit")
        print("="*40)
        choice = input("Enter your choice: ")

        if   choice == "1": add_patient()
        elif choice == "2": view_patients()
        elif choice == "3": view_doctors()
        elif choice == "4": book_appointment()
        elif choice == "5": view_appointments()
        elif choice == "6": search_patient()
        elif choice == "7": update_appointment_status()
        elif choice == "0":
            print("\n👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()