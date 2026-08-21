import os
from db import db
import streamlit as st

st.title("Patas e Laços - Cadastro de Pets")

with st.form("formCadastroPets"):
  col1, col2 = st.columns(2)

  with col1:
    nome = st.text_input("Nome*", placeholder="Digite o nome do pet")
    raca = st.text_input("Raça*", placeholder="Digite a raça do pet")
    idade = st.number_input("Idade (anos)*", min_value=0, max_value=30, step=1)

  with col2:
    porte = st.segmented_control(
        "Porte", options=["Pequeno", "Médio", "Grande"]
    )
    sexo = st.segmented_control("Sexo*", options=["Macho", "Fêmea"])
    status_adocao = st.segmented_control(
        "Status de Adoção*", options=["Disponível", "Adotado"]
    )

  descricao = st.text_area(
      "Descrição", placeholder="Digite uma breve descrição do pet"
  )
  foto = st.file_uploader("Foto do Pet", type=["jpg", "jpeg", "png"])

  if st.form_submit_button(
      "Cadastrar pet", type="primary", use_container_width=True
  ):
    if not nome:
      st.error("Preencha o nome")
    elif not raca:
      st.error("Preencha a raça")
    elif not sexo:
      st.error("Preencha o sexo")
    elif not status_adocao:
      st.error("Preencha o status de adoção")
    else:
      caminho_salvo = ""
      if foto is not None:
        caminho_salvo = os.path.join("uploads", foto.name)
        with open(caminho_salvo, "wb") as f:
          f.write(foto.read())

      novoPet = db.collection("pets").document()
      novoPet.set({
          "nome": nome,
          "raca": raca,
          "idade": int(idade),
          "porte": porte,
          "sexo": sexo,
          "status_adocao": status_adocao,
          "descricao": descricao,
          "foto": caminho_salvo,
      })

      st.success("Pet cadastrado com sucesso!")
      st.balloons()