import streamlit as st
import pandas as pd
from datetime import datetime
import os

# Excel filename
EXCEL_FILE = "checkin_log.xlsx"

# for it to pop up on the sidebar
st.sidebar.markdown("# Check-In Form 📋")

# Title
st.title("Check-In Form 📋")

# Section 1: Text Inputs
st.header("Personnel Info")
st_unit = st.text_input("ST/Unit")
last_name = st.text_input("Last Name")
first_name = st.text_input("First Name")
position = st.text_input("Position/Title")
cell_phone = st.text_input("Cell Phone #")
email = st.text_input("Email")
departure_point = st.text_input("Departure Point")
remarks = st.text_area("Remarks")

# Section 2: Dropdown
st.header("Transportation")
transportation = st.selectbox("Select Transportation", ["POV", "Rental", "Van", "Bus", "Other"])

# Section 3: Date & Time Inputs
st.header("Timing Info")
etd = st.time_input("ETD (Estimated Time of Departure)")
eta = st.time_input("ETA (Estimated Time of Arrival)")
date_ordered = st.date_input("Date Ordered")
time_ordered = st.time_input("Time Ordered")

# Submit Button
if st.button("Submit"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = {
        "Timestamp": timestamp,
        "ST/Unit": st_unit,
        "Last Name": last_name,
        "First Name": first_name,
        "Position/Title": position,
        "Cell Phone": cell_phone,
        "Email": email,
        "Departure Point": departure_point,
        "Remarks": remarks,
        "Transportation": transportation,
        "ETD": etd.strftime("%H:%M"),
        "ETA": eta.strftime("%H:%M"),
        "Date Ordered": date_ordered.strftime("%Y-%m-%d"),
        "Time Ordered": time_ordered.strftime("%H:%M"),
    }

    df_new = pd.DataFrame([data])

    if os.path.exists(EXCEL_FILE):
        df_existing = pd.read_excel(EXCEL_FILE)
        df_combined = pd.concat([df_existing, df_new], ignore_index=True)
    else:
        df_combined = df_new

    df_combined.to_excel(EXCEL_FILE, index=False)

    st.success("Check-in submitted and saved to Excel!")

