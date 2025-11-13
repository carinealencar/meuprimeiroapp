import streamlit as st

st.title('Meu primeiro APP 🤳')

st.header('Vamos fazer algo interativo')

n = st.number_input('Insira o número')
st.write(f'O número que você digitou elevado ao quadrado é {n**2}')