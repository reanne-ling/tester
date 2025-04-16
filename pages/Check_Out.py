import streamlit as st
import pandas as pd
from datetime import datetime
import os


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