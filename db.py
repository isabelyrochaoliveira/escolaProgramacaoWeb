import json
import os
from google.cloud import firestore
from google.oauth2 import service_account
import streamlit as st


def get_firestore_client():
  # 1. Se estiver rodando no Streamlit Cloud com Secrets
  try:
    if "FIREBASE_JSON" in st.secrets:
      info = json.loads(st.secrets["FIREBASE_JSON"])
      creds = service_account.Credentials.from_service_account_info(info)
      return firestore.Client(credentials=creds)
  except Exception:
    pass

  # 2. Se o arquivo firebase.json existir localmente
  if os.path.exists("firebase.json"):
    return firestore.Client.from_service_account_json("firebase.json")

  st.error("Credenciais do Firebase não encontradas!")
  st.stop()


db = get_firestore_client()