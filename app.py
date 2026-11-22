import streamlit as st

st.title("Conversor de temperatura")

modo = st.radio("Convertir de:", ["Celsius a fahrenheit", "fahrenheit a celsius"])
valor = st.number_input("Valor")

if modo == "Celsius a fahrenheit":
    resultado = valor * 9 / 5 + 32
    st.write(f"{valor} ºC son {resultado} ºf")
else:
    resultado = (valor - 32) * 5 / 9
    st.write(f"{valor} ºF son {resultado} ºC")