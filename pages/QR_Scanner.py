import streamlit as st
import pandas as pd
from datetime import datetime
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
import cv2
from pyzbar import pyzbar
import os

# needed to enter this into terminal to run:
    # pip install streamlit-webrtc opencv-python pyzbar

EXCEL_FILE = "qr_checkin_log.xlsx"

# Title
st.title("📷 QR Code Check-In System")

st.markdown("Scan your QR code to check in. The app will capture your ID and timestamp it.")

# Class to process video stream and detect QR codes
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

# Start the webcam scanner
ctx = webrtc_streamer(key="qr-checkin", video_transformer_factory=QRScanner)

if ctx.video_transformer:
    qr_data = ctx.video_transformer.qr_data
    if qr_data:
        st.success(f"✅ Scanned ID: {qr_data}")

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Save to Excel
        new_data = pd.DataFrame([{
            "Scanned ID": qr_data,
            "Check-In Time": timestamp
        }])

        if os.path.exists(EXCEL_FILE):
            existing_data = pd.read_excel(EXCEL_FILE)
            combined_data = pd.concat([existing_data, new_data], ignore_index=True)
        else:
            combined_data = new_data

        combined_data.to_excel(EXCEL_FILE, index=False)
        st.info("Saved to Excel!")

        # Reset qr_data so it doesn't keep saving
        ctx.video_transformer.qr_data = None


# footer
st.markdown("---")
st.caption("Provided by SJSU • Powered by Streamlit ")