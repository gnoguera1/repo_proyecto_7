import streamlit as st
import pandas as pd
import plotly.express as px

file=pd.read_csv('/Users/glorinoguera/Documents/TripleTen_curso/_PROYECTOS_/Proyecto_7/vehicles_us.csv')

st.header('Datos de Carros')

st.dataframe(file)
columnas=['price', 'model_year', 'model', 'condition', 'cylinders', 'fuel',
       'odometer', 'transmission', 'type', 'paint_color', 'is_4wd',
       'date_posted', 'days_listed']

columna= st.selectbox('Columna a elegir',columnas)
boton= st.button('Crear histograma')


if boton:
    st.markdown('## **Histograma**')

    car_hist=px.histogram(file,x=columna)
    st.plotly_chart(car_hist)


columns1=st.selectbox('Elige una columna',columnas)
boton2= st.button('Crear gráfico de dispersión')

if boton2:
   st.markdown('## **Gráfico de dispersión**')
   st.write(f'{columns1} vs. Price')
   car_disp=px.scatter(file,x=columns1,y='price')
   st.plotly_chart(car_disp)