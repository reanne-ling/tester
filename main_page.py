import streamlit as st
import pandas as pd 
import numpy as np
import openai

from datetime import datetime
import os

# for it to pop up on the sidebar
st.sidebar.markdown("# Home 🏠")


# title
st.title('EOC Check-In/Check-Out System')

# introduction
st.write = "Hi! Welcome to EOC's Check-In/Check Out System"
st.write += "Please come and explore our applications for your needs!"

# for table of contents
st.subheader('Table of Contents', divider= 'blue')
message = "Come explore our pages! We aim to help make sure you are registered properly." 
col1, col2 = st.columns(2)
with col1:
   st.page_link("pages/Check_In_Form.py", label="Check In Form", icon="📋")
   st.page_link("pages/page_2.py", label="AI Intake Assistant", icon="🧠")
   st.page_link("pages/page_3.py", label="AI Housing Chat Assistant", icon="💬")
   st.page_link("pages/page_4.py", label="Resources & Help", icon="🆘")
   st.page_link("pages/page_5.py", label="Language & Communication Tools", icon="💬")


with col2:
   st.page_link("pages/page_6.py", label="Reddit Sentiment Analyzer", icon="🔒")
   st.page_link("pages/page_7.py", label="AI Resource Recommender", icon="🎯")
   st.page_link("pages/page_8.py", label="Stakeholder Involvement", icon="🤝")
   st.page_link("pages/page_9.py", label="EIH Budget Overview", icon="💰")

# footer
st.markdown("---")
st.caption("Provided by SJSU")