import os
from google.cloud import firestore
import streamlit as st

db = firestore.Client.from_service_account_json("firebase.json")

st.title("Pets Disponíveis para Adoção")
st.write("Conheça os animaizinhos que estão à procura de um lar cheio de amor!")

with st.expander("Filtrar Pets", expanded=True):
  col_f1, col_f2, col_f3 = st.columns(3)

  with col_f1:
    filtro_status = st.selectbox(
        "Status", options=["Todos", "Disponível", "Adotado"], index=1
    )
  with col_f2:
    filtro_porte = st.selectbox(
        "Porte", options=["Todos", "Pequeno", "Médio", "Grande"]
    )
  with col_f3:
    filtro_sexo = st.selectbox("Sexo", options=["Todos", "Macho", "Fêmea"])

pets_stream = db.collection("pets").stream()
todos_pets = []

for pet_ref in pets_stream:
  dados = pet_ref.to_dict()
  dados["id"] = pet_ref.id
  todos_pets.append(dados)

pets_filtrados = [
    p
    for p in todos_pets
    if (filtro_status == "Todos" or p.get("status_adocao") == filtro_status)
    and (filtro_porte == "Todos" or p.get("porte") == filtro_porte)
    and (filtro_sexo == "Todos" or p.get("sexo") == filtro_sexo)
]

st.markdown(f"**Exibindo {len(pets_filtrados)} pet(s)**")
st.divider()

if not pets_filtrados:
  st.info("Nenhum pet encontrado com os filtros selecionados.")
else:
  colunas_por_linha = 3

  for i in range(0, len(pets_filtrados), colunas_por_linha):
    cols = st.columns(colunas_por_linha)
    grupo_pets = pets_filtrados[i : i + colunas_por_linha]

    for col, pet in zip(cols, grupo_pets):
      with col:
        if pet.get("foto") and os.path.exists(pet["foto"]):
          st.image(pet["foto"], use_container_width=True)

        st.subheader(pet.get("nome", "Sem Nome"))
        st.caption(
            f"**Raça:** {pet.get('raca', '')} | **Porte:**"
            f" {pet.get('porte', '')}"
        )
        st.caption(
            f"**Sexo:** {pet.get('sexo', '')} | **Idade:**"
            f" {pet.get('idade', 0)} ano(s)"
        )
        st.write(pet.get("descricao", ""))

        if pet.get("status_adocao") == "Disponível":
          st.success("Disponível para adoção")
          if st.button(
              f"Quero adotar {pet.get('nome')}!",
              key=f"btn_{pet['id']}",
              type="primary",
              use_container_width=True,
          ):
            st.balloons()
            st.success(
                f"Parabéns pelo interesse em adotar **{pet.get('nome')}**! A"
                " equipe entrará em contato."
            )
        else:
          st.error("Já foi adotado")