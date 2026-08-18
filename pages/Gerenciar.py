import streamlit as st

st.title("Gerenciar e Editar Pets")
st.write("Selecione um animal para atualizar o status ou editar as informações cadastradas.")

# Dados simulados apenas para teste
pets_simulados = {
    1: {
        "nome": "Thor",
        "porte": "Médio",
        "raca": "Vira-lata (SRD)",
        "sexo": "Macho",
        "idade": 2,
        "status": "Disponível",
        "descricao": "Muito dócil, brincalhão e se dá bem com outros cães."
    },
    2: {
        "nome": "Luna",
        "porte": "Pequeno",
        "raca": "Siamês",
        "sexo": "Fêmea",
        "idade": 1,
        "status": "Disponível",
        "descricao": "Tranquila, adora carinho e fica bem em apartamento."
    },
    3: {
        "nome": "Pipoca",
        "porte": "Grande",
        "raca": "Labrador",
        "sexo": "Macho",
        "idade": 4,
        "status": "Adotado",
        "descricao": "Enérgico e adora passear."
    }
}

opcoes_pets = {f"{dados['nome']} (ID #{id_pet})": id_pet for id_pet, dados in pets_simulados.items()}
selecionado = st.selectbox("Selecione o pet que deseja gerenciar:", options=list(opcoes_pets.keys()))

if selecionado:
    id_pet_escolhido = opcoes_pets[selecionado]
    pet = pets_simulados[id_pet_escolhido]

    st.divider()

    with st.form("form_edicao_pet"):
        st.subheader(f"Editando dados de: {pet['nome']}")

        col1, col2 = st.columns(2)
        
        with col1:
            nome_edit = st.text_input("Nome", value=pet["nome"])
            raca_edit = st.text_input("Raça", value=pet["raca"])
            idade_edit = st.number_input("Idade (anos)", min_value=0, max_value=30, value=pet["idade"], step=1)
        
        with col2:
            porte_edit = st.segmented_control("Porte", options=["Pequeno", "Médio", "Grande"], default=pet["porte"])
            sexo_edit = st.segmented_control("Sexo", options=["Macho", "Fêmea"], default=pet["sexo"])
            status_edit = st.segmented_control("Status de Adoção", options=["Disponível", "Adotado"], default=pet["status"])

        descricao_edit = st.text_area("Descrição", value=pet["descricao"])

        salvar = st.form_submit_button("Salvar Alterações")

        if salvar:
            if not nome_edit or not raca_edit:
                st.error("Preencha todos os campos obrigatórios (Nome e Raça).")
            else:
                st.success(f"Dados de **{nome_edit}** atualizados com sucesso!")
                if status_edit == "Adotado" and pet["status"] != "Adotado":
                    st.balloons()

    st.divider()


    st.subheader("Zona de Exclusão")
    st.caption("Esta ação removerá o cadastro do sistema.")
    

    if st.button("Excluir Pet", type="primary"):
         st.success(f"O registro de **{pet['nome']}** foi excluído com sucesso!")