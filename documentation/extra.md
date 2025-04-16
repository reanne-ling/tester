# this is supposed to be the way for us to connect to a google drive and then to a google sheet

    import gspread
    from oauth2client.service_account import ServiceAccountCredentials

    Set up the Google API credentials
        scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
        client = gspread.authorize(creds)

    Open the sheet (by title or URL)
        spreadsheet = client.open("Check-In Log")  # Replace with your sheet name
        sheet = spreadsheet.sheet1  # Use first sheet

    Load the data into a pandas DataFrame
        data = sheet.get_all_records()
        df_existing = pd.DataFrame(data)

# this is extra notes that we can add to the check in form which will aim to open up the chek out area after they submit. 

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


# this is for the QR code generation

    # install the package
        pip install streamlit-webrtc

    #