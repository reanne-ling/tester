# this will be a page that is accessible for admins and the team to create qr codes. 
import streamlit as st

# for it to pop up on the sidebar
st.sidebar.markdown("# QR Code Generator (icon)")

# Title
st.title("QR Code Generator (icon)")
st.caption("for testing purposes the password is: admin")

# Simple login simulation (optional)
admin_password = st.text_input("Enter admin password", type="password")
if admin_password != "admin": # this is where you enter in your password
    st.warning("Enter correct password to view logs.")
    st.stop()


# footer
st.markdown("---")
st.caption("Provided by SJSU • Powered by Streamlit ")