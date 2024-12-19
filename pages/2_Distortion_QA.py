import streamlit as st
import gspread

print()

credentials = {
    "project_id": st.secrets["project_id"],
    "private_key_id": st.secrets["project_id"],
    "private_key": st.secrets["private_key"],
    "client_email": st.secrets["client_email"],
    "client_id": st.secrets["client_id"],
    "auth_uri": st.secrets["auth_uri"],
    "token_uri": st.secrets["token_uri"],
    "auth_provider_x509_cert_url": st.secrets["auth_provider_x509_cert_url"],
    "client_x509_cert_url": st.secrets["client_x509_cert_url"],
    "universe_domain": st.secrets["universe_domain"]
}
gc = gspread.service_account_from_dict(credentials)
sh = gc.open("QA Record")
print(sh.sheet1.get('A1'))

st.write(sh.sheet1.get('A2'))