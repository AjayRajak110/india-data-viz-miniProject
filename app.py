import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(layout="wide")

df = pd.read_csv('india.csv')

list_of_states = list(df['State'].unique())

list_of_states.insert(0,'Overall India')


st.sidebar.title('India Ka Data Viz')
selected_state = st.sidebar.selectbox('select a state',list_of_states)
primary = st.sidebar.selectbox('select primary parameter',sorted(df.columns[5:]))
secondary = st.sidebar.selectbox('select secondary parameter',sorted(df.columns[5:]))

plot = st.sidebar.button('Plot Graph')
if plot:

    st.text('Size Represents Primary parameter')
    st.text('colour Represents Secondary parameter')
    if selected_state == 'Overall India':
        fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", size=primary, color=secondary, zoom=4, size_max=35,
                                mapbox_style="carto-positron", width=1200, height=700, hover_name='State')
        st.plotly_chart(fig, use_container_width=True)
    else:
        state_df = df[df['State']==selected_state]
        fig = px.scatter_mapbox(state_df, lat="Latitude", lon="Longitude", size=primary, color=secondary, zoom=6, size_max=35,
                                mapbox_style="carto-positron", width=1200, height=700, hover_name='District')
        st.plotly_chart(fig, use_container_width=True)

