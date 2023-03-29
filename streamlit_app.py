import streamlit as st

# Define a interface do usuário
def main():
    st.title("Meu primeiro aplicativo Streamlit")
    st.write("Bem-vindo ao meu aplicativo!")
    name = st.text_input("Digite o seu nome:")
    st.write(f"Olá, {name}!")

if __name__ == "__main__":
    main()
