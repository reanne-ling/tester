import streamlit as st
import qrcode
from io import BytesIO
from PIL import Image

# Sidebar
st.sidebar.markdown("# QR Code Generator 🧾")

# Title
st.title("QR Code Generator 🧾")
st.caption("For testing purposes the password is: admin")

# Password protection
admin_password = st.text_input("Enter admin password", type="password")
if admin_password != "admin":
    st.warning("Enter correct password to generate QRs.")
    st.stop()

st.text("Please enter in the following information to generate a QR code:")

# Input fields
full_name = st.text_input("Full Name", placeholder="e.g., John Doe")
role = st.text_input("Position/Title", placeholder="e.g., Logistics Section Chief")
team = st.selectbox("Team", ["Gold", "Blue"])
custom_id = st.text_input("Employee ID or Custom Tag", placeholder="e.g., EOC123")

# Generate Button
if st.button("Generate QR Code"):
    if full_name and role and custom_id:
        qr_data = f"Name: {full_name}\nTitle: {role}\nTeam: {team}\nID: {custom_id}"
        
        # Generate QR Code
        qr_img = qrcode.make(qr_data)
        buffered = BytesIO()
        qr_img.save(buffered, format="PNG")
        img_bytes = buffered.getvalue()

        # Show QR code
        st.image(qr_img, caption="Scan this QR code", use_column_width=False)

        # Download button
        st.download_button(
            label="Download QR Code",
            data=img_bytes,
            file_name=f"{full_name.replace(' ', '_')}_QR.png",
            mime="image/png"
        )
    else:
        st.error("Please fill in all fields before generating a QR code.")

# Footer
st.markdown("---")
st.caption("Provided by SJSU • Powered by Streamlit")
