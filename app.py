import streamlit as st
import pandas as pd
import re
from datetime import date

from database import (
    create_table,
    insert_patient,
    get_patients,
    delete_patient
)

from openai_service import (
    generate_remark
)

# Create table if it doesn't exist
create_table()

st.title("🏥 Health Prediction Application")

# ==========================
# ADD PATIENT
# ==========================

st.header("Add Patient")

with st.form("patient_form"):

    name = st.text_input("Full Name")

    dob = st.date_input("Date of Birth")

    email = st.text_input("Email Address")

    glucose = st.number_input(
        "Glucose",
        min_value=0.0
    )

    haemoglobin = st.number_input(
        "Haemoglobin",
        min_value=0.0
    )

    cholesterol = st.number_input(
        "Cholesterol",
        min_value=0.0
    )

    submit = st.form_submit_button(
        "Predict & Save"
    )

if submit:

    email_pattern = (
        r'^[\w\.-]+@[\w\.-]+\.\w+$'
    )

    if not name.strip():

        st.error("Name is required")

    elif not re.match(
        email_pattern,
        email
    ):

        st.error("Invalid Email")

    elif dob > date.today():

        st.error(
            "DOB cannot be a future date"
        )

    else:

        with st.spinner(
            "Generating Prediction..."
        ):

            remark = generate_remark(
                glucose,
                haemoglobin,
                cholesterol
            )

        insert_patient(
            name,
            str(dob),
            email,
            glucose,
            haemoglobin,
            cholesterol,
            remark
        )

        st.success(
            "Patient Saved Successfully"
        )

        st.write("### AI Prediction")

        st.info(remark)

# ==========================
# VIEW PATIENTS
# ==========================

st.header("Patient Records")

patients = get_patients()

if patients:

    df = pd.DataFrame(
        patients,
        columns=[
            "ID",
            "Name",
            "DOB",
            "Email",
            "Glucose",
            "Haemoglobin",
            "Cholesterol",
            "Remarks"
        ]
    )

    search = st.text_input(
        "Search Patient by Name"
    )

    if search:

        df = df[
            df["Name"].str.contains(
                search,
                case=False,
                na=False
            )
        ]

    st.dataframe(
        df,
        use_container_width=True
    )

else:

    st.info(
        "No patient records found."
    )

# ==========================
# DELETE PATIENT
# ==========================

st.header("Delete Patient")

patient_id = st.number_input(
    "Patient ID",
    min_value=1,
    step=1
)

if st.button("Delete Patient"):

    delete_patient(patient_id)

    st.success(
        "Patient Deleted Successfully"
    )

    st.rerun()

st.header("Update Patient Remark")

update_id = st.number_input(
    "Patient ID to Update",
    min_value=1,
    key="update"
)

new_remark = st.text_area(
    "New Remark"
)

if st.button("Update Remark"):

    update_remark(
        update_id,
        new_remark
    )

    st.success(
        "Remark Updated"
    )
