import streamlit as st
import pandas as pd
from datetime import datetime
import os

import streamlit as st
import pandas as pd
from datetime import datetime
import os

# Excel filename
EXCEL_FILE = "checkin_log.xlsx"

# for it to pop up on the sidebar
st.sidebar.markdown("# Check-Out Form 📋")

# Title
st.title("Personnel Check-Out Form 📋")
st.caption("for testing purposes the password is: blue")

# Simple login simulation (optional)
admin_password = st.text_input("Enter password", type="password")
if admin_password != "blue": # this is where you enter in your password
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

# Check-out button
if st.button("Check-Out!"):
    if checkout_last_name and checkout_first_name:
        # Read the existing data from the Excel file
        if os.path.exists(EXCEL_FILE):
            df_existing = pd.read_excel(EXCEL_FILE)

            # Search for the corresponding row by Last Name and First Name
            idx = df_existing[(df_existing['Last Name'] == checkout_last_name) & (df_existing['First Name'] == checkout_first_name)].index

            if len(idx) > 0:
                # Record the Check-Out timestamp
                checkout_timestamp = datetime.now().strftime("%Y-%m-%d") + " " + checkout_time.strftime("%H:%M")

                # Add a new column for Check-Out Timestamp, only if it doesn't already exist
                if "Check-Out Timestamp" not in df_existing.columns:
                    df_existing["Check-Out Timestamp"] = None

                # Update the corresponding row with the Check-Out timestamp
                df_existing.at[idx[0], "Check-Out Timestamp"] = checkout_timestamp

                # Save the updated data back to Excel
                df_existing.to_excel(EXCEL_FILE, index=False)

                st.success(f"Check-out successful! {checkout_first_name} {checkout_last_name}'s check-out time has been recorded.")
            else:
                st.error("No matching record found for the provided name.")
        else:
            st.error("No check-in data found in the Excel file.")
    else:
        st.error("Please provide both first and last name for check-out.")

# footer
st.markdown("---")
st.caption("Provided by SJSU")