import streamlit as st

st.set_page_config(
    page_title="Issue Reporting",
    page_icon="🔧",
)

st.title("Issue Reporting")
st.markdown(
"""
If any scanner issues are noted please report them here. 
""")

ReporterName = st.text_input("Reporters Name")
Issue = st.text_area("Enter issue text, ⚠️ NO PATIENT INFORMATION MUST BE ENTERED HERE! ⚠️")
st.button("Submit", type="primary")