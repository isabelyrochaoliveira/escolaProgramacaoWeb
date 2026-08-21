import json
import os
from google.cloud import firestore
from google.oauth2 import service_account
import streamlit as st

def get_firestore_client():
    try:
        if "FIREBASE_JSON" in st.secrets:
            info = json.loads(st.secrets["FIREBASE_JSON"])
            creds = service_account.Credentials.from_service_account_info(info)
            return firestore.Client(credentials=creds)
    except FileNotFoundError:
        pass 
    except json.JSONDecodeError:
        st.error("Erro na nuvem: O texto do FIREBASE_JSON está faltando alguma aspa ou vírgula.")
        st.stop()
    except Exception:
        pass

    if os.path.exists("firebase.json"):
        return firestore.Client.from_service_account_json("firebase.json")

    st.error("Credenciais não encontradas. Verifique o secrets no Cloud ou o firebase.json local.")
    st.stop()

db = get_firestore_client()