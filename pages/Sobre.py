import streamlit as st

st.title("Sobre o Patas & Laços")

st.subheader("Conectando animais resgatados a lares responsáveis")


st.divider()


col_missao1, col_missao2 = st.columns(2)

with col_missao1:

    st.markdown("### Nossa Missão")

    st.write("""
        O **Patas & Laços** nasceu como uma iniciativa para facilitar e incentivar a adoção consciente de animais. 

        Nossa plataforma funciona como uma ponte entre protetores/ONGs e pessoas que desejam abrir as portas de suas casas para um novo companheiro.
        
        Acreditamos que todo animal merece carinho, respeito e um lar seguro para viver com dignidade.
        """)

with col_missao2:
    st.image("imgs/missao.jpg", use_container_width=True)


st.divider()


st.markdown("### Dicas para uma Adoção Consciente")

st.write("Antes de adotar, é fundamental avaliar alguns pontos essenciais:")

with st.expander("1. Vacinação e Cuidados Veterinários"):
    st.write("""
        Mantenha sempre as vacinas (V10/V8 para cães, V4/V5 para gatos e Antirrábica) e a vermifugação em dia. 
        Consultas periódicas com o médico-veterinário garantem qualidade de vida e prevenção de doenças.
        """)

with st.expander("2. Adaptação e Segurança do Ambiente"):
    st.write("""
        Para gatos, a instalação de **telas de proteção** em janelas e sacadas é indispensável. 
        Para cães, garanta que os portões e muros sejam seguros para evitar fugas acidentais.
        """)

with st.expander("3. Tempo, Paciência e Afeto"):
    st.write("""
        O período de adaptação de um animal resgatado pode levar de algumas semanas a meses. 
        Respeite o espaço e o ritmo do seu pet com paciência e reforço positivo.
        """)


st.divider()


st.markdown("### Autoria do Projeto")
st.caption("Desenvolvido para a Escola de Programação Web, com fins acadêmicos, utilizando Streamlit.")

st.info("Desenvolvido por Isabely Rocha de Oliveira, 2026")