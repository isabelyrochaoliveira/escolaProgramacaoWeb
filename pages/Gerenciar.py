import streamlit as st
from db import db

st.title("Gerenciar e Editar Pets")
st.write(
    "Selecione um animal para atualizar o status ou editar as informações cadastradas."
)

pets_stream = db.collection("pets").stream()
pets_dict = {}

for pet_ref in pets_stream:
    dados = pet_ref.to_dict()
    pets_dict[pet_ref.id] = dados

if not pets_dict:
    st.info("Nenhum pet cadastrado no banco de dados.")
else:
    opcoes_pets = {
      f"{dados.get('nome', 'Sem nome')} (ID #{doc_id[:6]})": doc_id
      for doc_id, dados in pets_dict.items()
    }

    selecionado = st.selectbox(
        "Selecione o pet que deseja gerenciar:", options=list(opcoes_pets.keys())
    )

    if selecionado:
        id_pet_escolhido = opcoes_pets[selecionado]
        pet = pets_dict[id_pet_escolhido]

        status_atual = pet.get("status_adocao") or pet.get("status", "Disponível")
        porte_atual = pet.get("porte", "Médio")
        sexo_atual = pet.get("sexo", "Macho")

        with st.form("form_edicao_pet"):
            st.subheader(f"Editando dados de: {pet.get('nome')}")

            col1, col2 = st.columns(2)

            with col1:
                nome_edit = st.text_input("Nome*", value=pet.get("nome", ""))
                raca_edit = st.text_input("Raça*", value=pet.get("raca", ""))
                idade_edit = st.number_input(
                    "Idade (anos)*",
                    min_value=0,
                    max_value=30,
                    value=int(pet.get("idade", 0)),
                    step=1,
                )

            with col2:
                porte_edit = st.segmented_control(
                    "Porte",
                    options=["Pequeno", "Médio", "Grande"],
                    default=porte_atual,
                )
                sexo_edit = st.segmented_control(
                    "Sexo",
                    options=["Macho", "Fêmea"],
                    default=sexo_atual,
                )
                status_edit = st.segmented_control(
                    "Status de Adoção",
                    options=["Disponível", "Adotado"],
                    default=status_atual,
                )

            descricao_edit = st.text_area(
                "Descrição", value=pet.get("descricao", "")
            )

            salvar = st.form_submit_button(
                "Salvar Alterações", type="primary", use_container_width=True
            )

            if salvar:
                if not nome_edit or not raca_edit:
                    st.error("Preencha todos os campos obrigatórios (Nome e Raça).")
                else:
                    doc_ref = db.collection("pets").document(id_pet_escolhido)
                    doc_ref.update(
                        {
                            "nome": nome_edit,
                            "raca": raca_edit,
                            "idade": int(idade_edit),
                            "porte": porte_edit,
                            "sexo": sexo_edit,
                            "status_adocao": status_edit,
                            "descricao": descricao_edit,
                        }
                    )

                    st.success(f"Dados de **{nome_edit}** atualizados com sucesso!")
                    if status_edit == "Adotado" and status_atual != "Adotado":
                        st.balloons()
                    st.rerun()

        st.divider()

        st.subheader("Zona de Exclusão")
        st.caption("Esta ação removerá o cadastro definitivamente do banco de dados.")

        if st.button(
            f"Excluir registro de {pet.get('nome')}",
            type="primary",
            use_container_width=True,
        ):
            db.collection("pets").document(id_pet_escolhido).delete()
            st.success(f"O registro de **{pet.get('nome')}** foi excluído com sucesso!")
            st.rerun()