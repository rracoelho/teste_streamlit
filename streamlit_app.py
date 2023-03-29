import streamlit as st

# Botão
if st.button("Clique aqui"):
    st.write("Botão clicado!")

# Caixa de seleção
option = st.selectbox(
    "Escolha uma opção",
    ["Opção 1", "Opção 2", "Opção 3"]
)
st.write("Você escolheu a opção:", option)

# Slider
value = st.slider("Escolha um valor", 0, 100)
st.write("Você escolheu o valor:", value)
