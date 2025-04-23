import streamlit as st
import pandas as pd
from datetime import datetime

# Google Sheets integration
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from sheets_connector import connect_to_google_sheet
from gspread_dataframe import get_as_dataframe, set_with_dataframe

# Connect to the Google Sheet
sheet = connect_to_google_sheet()
df_existing = get_as_dataframe(sheet).fillna("")

# for it to pop up on the sidebar
st.sidebar.markdown("# Check-Out Form 📋")

# Title
st.title("Personnel Check-Out Form 📋")
st.caption("for testing purposes the password is: gold")

# Simple login simulation (optional)
admin_password = st.text_input("Enter password", type="password")
if admin_password != "gold": # this is where you enter in your password
    st.warning("Enter correct password to access this form.")
    st.stop()

st.text('Please enter the following information to record check-out time.')

# Input fields for First Name, Last Name, and Check-Out Time
checkout_last_name = st.text_input("Last Name", placeholder='e.g., Doe')
checkout_first_name = st.text_input("First Name", placeholder='e.g., John')

# Input for Check-Out Time
st.text('Time of Check-Out')
st.text('time will be recorded on military time')
col1, col2 = st.columns(2)
with col1:
    order_date = st.date_input("Date", key="out_date")
with col2:
    order_time = st.time_input("Time", key="out_time")

# Confirmation checkbox
confirm_checkout = st.checkbox("I confirm that I am checking out.")

# Check-out button
if st.button("Check-Out!") and confirm_checkout:
    if checkout_last_name and checkout_first_name:
        # Search for the matching entry
        idx = df_existing[
            (df_existing['Last Name'].str.lower() == checkout_last_name.lower()) &
            (df_existing['First Name'].str.lower() == checkout_first_name.lower())
        ].index

        if len(idx) > 0:
            # Record Check-Out timestamp
            checkout_timestamp = order_date.strftime("%Y-%m-%d") + " " + order_time.strftime("%H:%M")

            if "Check-Out Timestamp" not in df_existing.columns:
                df_existing["Check-Out Timestamp"] = ""

            df_existing.at[idx[0], "Check-Out Timestamp"] = checkout_timestamp

            # Write back to Google Sheets
            set_with_dataframe(sheet, df_existing)

            st.success(f"Check-out successful! {checkout_first_name} {checkout_last_name}'s time has been recorded.")
        else:
            st.error("No matching record found for the provided name.")
    else:
        st.error("Please provide both first and last name to check out.")

# footer
st.markdown("---")
st.caption("Provided by SJSU • Powered by Streamlit ")
