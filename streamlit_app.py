import os
import requests
import streamlit as st
from streamlit_lottie import st_lottie

try:
  if "FIREBASE_JSON" in st.secrets and not os.path.exists("firebase.json"):
    with open("firebase.json", "w", encoding="utf-8") as f:
      f.write(st.secrets["FIREBASE_JSON"])
except Exception:
  pass

def carregar_animacao(url: str):
    requisicao = requests.get(url)
    if requisicao.status_code != 200:
        return None
    return requisicao.json()


st.title("Patas e Laços - Conectando corações a quatro patas")
st.subheader("Sua plataforma de adoção responsável e transformação de vidas")

st.divider()

col_animacao, col_texto = st.columns(2)

with col_animacao:
    url_lottie = ("https://lottie.host/a631f69e-b758-4891-a9e1-ed662325e94c/QK2EAIBRAX.json")
    animacao_pet = carregar_animacao(url_lottie)

    if animacao_pet:
        st_lottie(animacao_pet, height=320, key="lottie_inicio")

    else:
        st.info("Carregando animação...")

with col_texto:
    st.subheader("Por que adotar?")
    st.markdown(
        """
        Milhares de animais aguardam a chance de ter uma família. Ao adotar, você não apenas
        ganha um companheiro leal, mas também abre espaço para que novos resgates aconteçam.

        **Como funciona a plataforma?**
        1. **Explore:** Acesse a aba *Ver Pets* para conhecer os animais disponíveis.
        2. **Cadastre:** Se você é uma ONG ou protetor, use a aba *Cadastrar Pet*.
        3. **Acompanhe:** Mantenha os dados e status de adoção atualizados na aba *Gerenciar*.
        4. **Saiba mais:** Acesse a aba *Sobre* para conhecer mais sobre a plataforma.
        """
    )
