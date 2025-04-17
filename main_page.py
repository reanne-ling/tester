import streamlit as st
import pandas as pd 
import numpy as np

from datetime import datetime
# import os
# import gspread


# for it to pop up on the sidebar
st.sidebar.markdown("# Home 🏠")


# title
st.title('EOC Check-In/Check-Out System')

# introduction
st.write = ("Hi! Welcome to EOC's Check-In/Check Out System")
st.write += ("Please come and explore our applications for your needs!")

# for table of contents
st.subheader('For Users', divider= 'blue')
st.text("Come explore our pages! We aim to help make sure you are registered properly.") 

col1, col2 = st.columns(2)
with col1:
   st.text("To scan your personal QR Codes:")
   st.text("for the GOLD Team:")
   st.page_link("pages/Gold_Check_In_Form.py", label="Check In Form", icon="📋")
   st.page_link("pages/Gold_Check_Out_Form.py", label="Check Out Form", icon="🔒")
with col2:
   st.page_link("pages/QR_Scanner.py", label="QR Scanner", icon="🔒")
   st.text("for the BLUE Team:")
   st.page_link("pages/Blue_Check_In_Form.py", label="Check In Form", icon="📋")
   st.page_link("pages/Blue_Check_Out_Form.py", label="Check Out Form", icon="🔒")

st.subheader('For Administrators', divider= 'blue')
col3, col4 = st.columns(2)
with col3:
   st.page_link("pages/Admin_DashBoard.py", label="Admin DashBoard", icon="🔒")
with col4:
   st.page_link("pages/QR_Generator.py", label="QR Generator", icon="🔒")

# footer
st.markdown("---")
st.caption("Provided by SJSU • Powered by Streamlit ")