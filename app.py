# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 13:05:48 2024

@author: franc
"""



import streamlit as st

st.title('Cálculo sencillo')

# Input fields for the user to enter values
value1 = st.number_input('Ingresar 1er valor', value=0.0)
value2 = st.number_input('Ingresar 2do valor', value=0.0)

# Button to perform the calculation
if st.button('Calcular'):
    result = value1 + value2
    st.write(f'La suma de  {value1} y {value2} es en total igual a {result}')
