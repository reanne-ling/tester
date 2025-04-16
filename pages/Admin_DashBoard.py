import streamlit as st
import pandas as pd
import os

EXCEL_FILE = "checkin_log.xlsx"

st.title("Admin Log Viewer")
st.caption("for testing purposes the password is: admin")

# Simple login simulation (optional)
admin_password = st.text_input("Enter admin password", type="password")
if admin_password != "admin": # this is where you enter in your password
    st.warning("Enter correct password to view logs.")
    st.stop()

if os.path.exists(EXCEL_FILE):
    df = pd.read_excel(EXCEL_FILE)

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
    st.download_button("Download Excel File", df.to_excel(index=False), file_name="checkin_log.xlsx")
else:
    st.error("No log file found yet.")

# footer
st.markdown("---")
st.caption("Provided by SJSU")