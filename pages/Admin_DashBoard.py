import streamlit as st
import pandas as pd
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from sheets_connector import connect_to_google_sheet
from gspread_dataframe import get_as_dataframe, set_with_dataframe

# for it to pop up on the sidebar
st.sidebar.markdown("# Administration DashBoards 🔒")

st.title("Admin Log Viewer")
st.caption("for testing purposes the password is: admin")

# Simple login simulation (optional)
admin_password = st.text_input("Enter admin password", type="password")
if admin_password != "admin": # this is where you enter in your password
    st.warning("Enter correct password to view logs.")
    st.stop()

st.caption('this page should provide you a space to be able to view logs and filter out the records based on the excel/google sheet')

# ✅ Connect to the Google Sheet
try:
    sheet = connect_to_google_sheet()
    df = get_as_dataframe(sheet)

    # Show full log
    st.subheader("Full Check-In/Check-Out Logs")
    st.dataframe(df)

    # Optional: Add filter options
    st.markdown("### Filter by Last Name")
    last_name_filter = st.text_input("Search by last name")
    if last_name_filter:
        filtered_df = df[df["Last Name"].str.contains(last_name_filter, case=False)]
        st.dataframe(filtered_df)

    st.markdown("### Download Logs")
    st.download_button("Download Log as CSV", df.to_csv(index=False), file_name="checkin_log.csv")
except Exception as e:
    st.error("No log file found yet.")

# footer
st.markdown("---")
st.caption("Provided by SJSU • Powered by Streamlit ")
