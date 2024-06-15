import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Proyecto 5. Herramientas de Desarrollo de Software')
st.subheader('Datos de anuncios de venta de vehículos')
st.write('¡Bienvenido a la herramienta interactiva para explorar datos de anuncios de venta de vehículos!')

st.subheader('Instrucciones')
st.write('Selecciona las opciones para visualizar los gráficos')

car_data = pd.read_csv('vehicles_us.csv') # lee los datos
build_histogram = st.checkbox('Construir un histograma') #casilla de verificación para crear un histograma
build_scatter = st.checkbox('Construir gráfico de dispersión') #casilla de verificación para crear un gráfico de dispersión

if build_histogram:  # al hacer clic en la casilla
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crea un histograma
    fig_hist = px.histogram(car_data, x="odometer", color="fuel", color_discrete_map={
        'Gasoline': 'red',
        'Diesel': 'orange',
        'Electric': 'green',
        'Hybrid': 'yellow'
    })

    # personaliza el diseño del gráfico
    fig_hist.update_layout(
        title='Histograma de Vehículos en Venta según Kilometraje',
        xaxis_title='Kilometraje',
        yaxis_title='Cantidad de Vehículos'
    )
    
    # muestra un gráfico Plotly interactivo
    st.plotly_chart(fig_hist, use_container_width=True)


if build_scatter: # al hacer click a la casilla
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    #crea un gráfico de dispersión
    fig_scatter = px.scatter(car_data, x="odometer", y="price", color="model_year", color_continuous_scale='Bluered_r') 

    # personaliza el diseño del gráfico
    fig_scatter.update_layout(
        title='Relación entre Kilometraje y Precio de Vehículos',
        xaxis_title='Kilometraje',
        yaxis_title='Precio de Vehículos'
    )

    # muestra un gráfico Plotly interactivo
    st.plotly_chart(fig_scatter, use_container_width=True)