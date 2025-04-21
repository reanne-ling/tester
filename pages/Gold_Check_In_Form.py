import streamlit as st
import pandas as pd
from datetime import datetime

# Google Sheets connection
from sheets_connector import connect_to_google_sheet
from gspread_dataframe import get_as_dataframe, set_with_dataframe


# for it to pop up on the sidebar
st.sidebar.markdown("# Check-In Form 📋")

# Title
st.title("Personnel Check-In Form 📋")
st.caption("for testing purposes the password is: gold")

# Simple login simulation (optional)
admin_password = st.text_input("Enter password", type="password")
if admin_password != "gold": # this is where you enter in your password
    st.warning("Enter correct password to access this form.")
    st.stop()

st.text('Please enter in the following information')

# ICS 219-5 Personnel
st.header("ICS 219-5 Personnel", divider='blue')

st_unit = st.text_input("ST/Unit", placeholder='e.g., Unit Name')

col7, col8 = st.columns(2)
with col7:
    last_name = st.text_input("Last Name", placeholder='e.g., Doe')
with col8:
    first_name = st.text_input("First Name", placeholder='e.g., John')

position = st.text_input("Position/Title", placeholder='e.g., Your Job Title')
primary_cell = st.text_input("Primary Contact Information (Cell Phone #)", placeholder='e.g., (123)456-7890')
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
    # based on devin's there is also
        # POV (personal vehicle),
        # AOV (assigned vehicle), 
other = st.text_input("If Other:", placeholder='bus')

st.text('Date/Time Ordered')
col5, col6 = st.columns(2)
with col5:
    order_date = st.date_input("Date", key="order_date")
with col6:
    order_time = st.time_input("Time", key="order_time")

remarks = st.text_area("Remarks", placeholder='e.g., Position Title')

# EOC Check-in List (EOC 211)
st.header("EOC Check-in List (EOC 211)", divider='blue')
st.subheader("Incident Contact Information")

cell_phone = st.text_input("Cell Phone #", placeholder='e.g., (123)456-7890')
email = st.text_input("Email", placeholder='e.g., john.doe@sanjoseca.gov')

# For verification
st.header("For verification", divider="blue")
st.text("by digitally signing this form, you are agreeing that this is information is correct and accurate")
signature = st.text_input("Signature", placeholder='e.g., Your Name')


# Submit Button
if st.button("Submit"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = {
        "Timestamp": timestamp,
        "ST/Unit": st_unit,
        "Last Name": last_name,
        "First Name": first_name,
        "Position/Title": position,
        "Primary Contact Information": primary_cell,
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

# footer
st.markdown("---")
st.caption("Provided by SJSU • Powered by Streamlit ")
