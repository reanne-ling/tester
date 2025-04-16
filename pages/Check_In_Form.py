import streamlit as st
import pandas as pd
from datetime import datetime
import os

    # import gspread
    # from oauth2client.service_account import ServiceAccountCredentials

# Excel filename
EXCEL_FILE = "checkin_log.xlsx"

# Set up the Google API credentials
    # scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    # creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    # client = gspread.authorize(creds)

# Open the sheet (by title or URL)
    # spreadsheet = client.open("Check-In Log")  # Replace with your sheet name
    # sheet = spreadsheet.sheet1  # Use first sheet

# for it to pop up on the sidebar
st.sidebar.markdown("# Check-In Form 📋")

# Title
st.title("Check-In Form 📋")

st.header("Personnel Info", divider='blue')
st.text('Please enter in the following information')

# Section 1: Text Inputs
st_unit = st.text_input("ST/Unit", placeholder='e.g., Unit Name')
last_name = st.text_input("Last Name", placeholder='e.g., Doe')
first_name = st.text_input("First Name", placeholder='e.g., John')
position = st.text_input("Position/Title", placeholder='e.g., Manager')
cell_phone = st.text_input("Cell Phone #", placeholder='e.g., (123)456-7890')
email = st.text_input("Email", placeholder='e.g., john.doe@sanjoseca.gov')
departure_point = st.text_input("Departure Point", placeholder='e.g., point')

st.text('ETD (Estimated Time of Departure)')
col1, col2 = st.columns(2)
with col1:
    etd_date = st.date_input("Date", key="etd_date")
with col2:
    etd_time = st.time_input("Time", key="etd_time")

st.text('ETA (Estimated Time of Arrival)')
col3, col4 = st.columns(2)
with col3:
    eta_date = st.date_input("Date", key="eta_date")
with col4:
    eta_time = st.time_input("Time", key="eta_time")

transportation = st.selectbox("Select Transportation", ["Vehicle", "Bus", "Air", "Other"], placeholder='Bus')
other = st.text_input("If Other:", placeholder='bus')

st.text('Date/Time Ordered')
col5, col6 = st.columns(2)
with col5:
    order_date = st.date_input("Date", key="order_date")
with col6:
    order_time = st.time_input("Time", key="order_time")

remarks = st.text_area("Remarks", placeholder='e.g., Position Title')

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
        "ETD": f"{etd_date.strftime('%m/%d/%Y')} {etd_time.strftime('%H:%M')}",
        "ETA": f"{eta_date.strftime('%m/%d/%Y')} {eta_time.strftime('%H:%M')}",
        "Date/Time Ordered": f"{order_date.strftime('%m/%d/%Y')} {order_time.strftime('%H:%M')}"
    }

    df_new = pd.DataFrame([data])

    if os.path.exists(EXCEL_FILE):
        df_existing = pd.read_excel(EXCEL_FILE)
        df_combined = pd.concat([df_existing, df_new], ignore_index=True)
    else:
        df_combined = df_new

    df_combined.to_excel(EXCEL_FILE, index=False)

    st.success("Check-in submitted and saved to Excel!")


# Check-Out Section (Only visible if Check-in data exists)
if "checkin_data" in st.session_state:
    st.header("Check-Out Section")
    st.text(f"Welcome back, {st.session_state.checkin_data['First Name']} {st.session_state.checkin_data['Last Name']}!")

    # Check-out button
    if st.button("Check-Out"):
        checkout_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        checkout_data = {
            "Timestamp": checkout_timestamp,
            "Check-Out": f"{checkout_timestamp}"
        }

        # Optionally, you can add the check-out data to the same Excel sheet.
        df_checkout = pd.DataFrame([checkout_data])

        if os.path.exists(EXCEL_FILE):
            df_existing = pd.read_excel(EXCEL_FILE)
            df_combined = pd.concat([df_existing, df_checkout], ignore_index=True)
        else:
            df_combined = df_checkout

        df_combined

# Load the data into a pandas DataFrame
    # data = sheet.get_all_records()
    # df_existing = pd.DataFrame(data)