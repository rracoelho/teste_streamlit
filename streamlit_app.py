import streamlit as st
import numpy as np

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
value = st.slider("Escolha um valor", 1, 100)
st.write("Você escolheu o valor:", value)
         
# Dados de exemplo
x = np.linspace(0, 10, value)
y = np.sin(x)

st.line_chart(y)
