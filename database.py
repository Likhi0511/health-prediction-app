import sqlite3


def get_connection():

    conn = sqlite3.connect("health.db")

    return conn


def create_table():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS patients(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            full_name TEXT,

            dob TEXT,

            email TEXT,

            glucose REAL,

            haemoglobin REAL,

            cholesterol REAL,

            remarks TEXT
        )
    """)

    conn.commit()

    conn.close()


def insert_patient(
    full_name,
    dob,
    email,
    glucose,
    haemoglobin,
    cholesterol,
    remarks
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO patients(
            full_name,
            dob,
            email,
            glucose,
            haemoglobin,
            cholesterol,
            remarks
        )
        VALUES(?,?,?,?,?,?,?)
    """,(
        full_name,
        dob,
        email,
        glucose,
        haemoglobin,
        cholesterol,
        remarks
    ))

    conn.commit()

    conn.close()


def get_patients():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM patients"
    )

    data = cursor.fetchall()

    conn.close()

    return data

def update_patient(
    patient_id,
    remarks
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE patients
        SET remarks=?
        WHERE id=?
        """,
        (remarks, patient_id)
    )

    conn.commit()

    conn.close()


def delete_patient(patient_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM patients WHERE id=?",
        (patient_id,)
    )

    conn.commit()

    conn.close()

def update_remark(patient_id, remark):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE patients
        SET remarks=?
        WHERE id=?
        """,
        (remark, patient_id)
    )

    conn.commit()
    conn.close()