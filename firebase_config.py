import firebase_admin
from firebase_admin import credentials, firestore, initialize_app
import streamlit as st
from google.cloud import firestore
from google.cloud.firestore import Client

# cred = credentials.Certificate('clave_json_firebase\proyectopinaldass-firebase-adminsdk-q0mci-b5f55f4c18.json')
# firebase_admin.initialize_app(cred)
# db = firestore.client()

# cred = credentials.Certificate({
#     "type": st.secrets["firebase"]["type"],
#     "project_id": st.secrets["firebase"]["project_id"],
#     "private_key_id": st.secrets["firebase"]["private_key_id"],
#     "private_key": st.secrets["firebase"]["private_key"].replace("\\n", "\n"),
#     "client_email": st.secrets["firebase"]["client_email"],
#     "client_id": st.secrets["firebase"]["client_id"],
#     "auth_uri": st.secrets["firebase"]["auth_uri"],
#     "token_uri": st.secrets["firebase"]["token_uri"],
#     "auth_provider_x509_cert_url": st.secrets["firebase"]["auth_provider_x509_cert_url"],
#     "client_x509_cert_url": st.secrets["firebase"]["client_x509_cert_url"]
# })

# initialize_app(cred)

# db = firestore.client()

def get_db():
    db=firestore.Client.from_service_account_json('key.json')
    return db