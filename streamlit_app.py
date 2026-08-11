import streamlit as st

st.title("Patas e Laços - Conectando corações a quatro patas")
st.subheader("Sua plataforma de adoção responsável e transformação de vidas.")

st.markdown("---")

col_img, col_texto = st.columns([1, 1])

with col_img: 
    st.image("imgs/conexao.jpg", caption="Adotar é um ato de amor responsável.")

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
        """
        )

        if st.button("🎉 Comemorar Adoções Recentes!"):
            st.balloons()

st.markdown("---")