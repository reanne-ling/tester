import streamlit as st
import pandas as pd
from datetime import datetime
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
import cv2
from pyzbar import pyzbar

# Google Sheets connector
from sheets_connector import connect_to_google_sheet
from gspread_dataframe import get_as_dataframe, set_with_dataframe

# Title
st.title("📷 QR Code Check-In System")
st.markdown("Scan your QR code to check in. The app will capture your ID and timestamp it.")

# QR Scanner logic
class QRScanner(VideoTransformerBase):
    def __init__(self):
        self.qr_data = None

    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")
        decoded_objects = pyzbar.decode(img)

        for obj in decoded_objects:
            self.qr_data = obj.data.decode("utf-8")
            (x, y, w, h) = obj.rect
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        return img

# Start webcam stream
ctx = webrtc_streamer(key="qr-checkin", video_transformer_factory=QRScanner)

if ctx.video_transformer:
    qr_data = ctx.video_transformer.qr_data
    if qr_data:
        st.success(f"✅ Scanned ID: {qr_data}")

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Data to be logged
        new_data = pd.DataFrame([{
            "Scanned ID": qr_data,
            "Check-In Time": timestamp
        }])

        try:
            # Connect to Google Sheet
            sheet = connect_to_google_sheet(sheet_name="QR Check-In Log")  # Use a specific sheet for QR logs
            existing_data = get_as_dataframe(sheet).dropna(how="all")
            combined_data = pd.concat([existing_data, new_data], ignore_index=True)
            set_with_dataframe(sheet, combined_data)

            st.info("✅ Check-in saved to Google Sheets!")
        except Exception as e:
            st.error(f"❌ Failed to save to Google Sheets: {e}")

        # Reset QR data so it doesn't keep saving repeatedly
        ctx.video_transformer.qr_data = None

# Footer
st.markdown("---")
st.caption("Provided by SJSU • Powered by Streamlit")
