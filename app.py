# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import plotly.graph_objects as go


car_data = pd.read_csv('vehicles_us.csv', encoding='utf-8')

build_histogram = st.checkbox('Construir histograma')

if build_histogram:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    fig.update_layout(title_text='Distribución del Odómetro')
    st.plotly_chart(fig, use_container_width=True)

build_scatter = st.checkbox('Construir gráfico de dispersión')

if build_scatter:

    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig1 = go.Figure(
        data=[go.Scatter(x=car_data['odometer'], y=car_data['price'], mode='markers')])
    fig1.update_layout(title_text='Relación entre Odómetro y Precio')
    st.plotly_chart(fig1, use_container_width=True)
