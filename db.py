import os
from google.cloud import firestore
from google.oauth2 import service_account
import streamlit as st

def get_firestore_client():
    try:
        if "firebase" in st.secrets:
            info = dict(st.secrets["firebase"]) 
            creds = service_account.Credentials.from_service_account_info(info)
            return firestore.Client(credentials=creds)
    except Exception:
        pass 

    if os.path.exists("firebase.json"):
        return firestore.Client.from_service_account_json("firebase.json")

    st.error("Credenciais não encontradas. Verifique os secrets no Cloud ou o firebase.json local.")
    st.stop()

db = get_firestore_client()