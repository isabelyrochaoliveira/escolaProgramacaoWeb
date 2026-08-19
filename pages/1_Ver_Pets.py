import os
import streamlit as st

st.title("Pets Disponíveis para Adoção")

st.write("Conheça os animaizinhos que estão à procura de um lar cheio de amor!")

# Lista de dados simulados apenas para teste
pets_simulados = {
    1: {
        "id": 1,
        "nome": "Thor",
        "porte": "Médio",
        "raca": "Vira-lata (SRD)",
        "sexo": "Macho",
        "idade": 2,
        "status": "Disponível",
        "descricao": "Muito dócil, brincalhão e se dá bem com outros cães.",
        "foto": "https://images.unsplash.com/photo-1560028913-5f8a8e836d7a?q=80&w=1738&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    },
    2: {
        "id": 2,
        "nome": "Luna",
        "porte": "Pequeno",
        "raca": "Siamês",
        "sexo": "Fêmea",
        "idade": 1,
        "status": "Disponível",
        "descricao": "Tranquila, adora carinho e fica bem em apartamento.",
        "foto": "https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?q=80&w=1686&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    },
    3: {
        "id": 3,
        "nome": "Pipoca",
        "porte": "Grande",
        "raca": "Labrador",
        "sexo": "Macho",
        "idade": 4,
        "status": "Adotado",
        "descricao": "Enérgico e adora passear.",
        "foto": "https://images.unsplash.com/photo-1552575595-38bfbd75841a?q=80&w=1738&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    },
}

with st.expander("Filtrar Pets", expanded=True):
    col_f1, col_f2, col_f3 = st.columns(3)

    with col_f1:
        filtro_status = st.selectbox("Status", options=["Todos", "Disponível", "Adotado"], index=1)

    with col_f2:
        filtro_porte = st.selectbox("Porte", options=["Todos", "Pequeno", "Médio", "Grande"])

    with col_f3:
        filtro_sexo = st.selectbox("Sexo", options=["Todos", "Macho", "Fêmea"])

pets_filtrados = [
    p
    for p in pets_simulados.values()
    if (filtro_status == "Todos" or p["status"] == filtro_status)
    and (filtro_porte == "Todos" or p["porte"] == filtro_porte)
    and (filtro_sexo == "Todos" or p["sexo"] == filtro_sexo)
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

                if pet["foto"]:
                    st.image(pet["foto"], use_container_width=True)

                st.subheader(pet["nome"])

                st.caption(f"**Raça:** {pet['raca']} | **Porte:** {pet['porte']}")

                st.caption(f"**Sexo:** {pet['sexo']} | **Idade:** {pet['idade']} ano(s)")

                st.write(pet["descricao"])

                if pet["status"] == "Disponível":
                    st.success("Disponível para adoção")
                    if st.button(f"Quero adotar {pet['nome']}!", key=f"btn_{pet['id']}", type="primary"):
                        st.balloons()
                        st.success( f"Parabéns pelo interesse em adotar **{pet['nome']}**! A equipe entrará em contato.")

                else:
                    st.error("Já foi adotado")