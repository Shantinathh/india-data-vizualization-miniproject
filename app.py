import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(layout="wide")


# to import the data
df = pd.read_csv('india.csv')
list_of_states = list(df['State'].unique())
list_of_states.insert(0,'Overall India')



st.sidebar.title('India map')
selected_state = st.sidebar.selectbox('Select state',list_of_states)
primary = st.sidebar.selectbox('Select primary parameter',sorted(df.columns[9:]))
secondary = st.sidebar.selectbox('Select secondary parameter',sorted(df.columns[9:]))


plot = st.sidebar.button('Plot Graph')

if plot:
    st.text('Size represents primary paramater')
    st.text('Color represents secondary paramater')

    # to plot for overall india
    if selected_state == 'Overall India':
        fig = px.scatter_map(df, lat='Latitude', lon='Longitude', zoom=3.5, map_style="carto-positron",size=primary,color=secondary,width=1500,height=560,hover_name='District')
        # to plot plotly in streamlit
        st.plotly_chart(fig,use_container_width=True)
    else:
        # plot for selected state
        state_df = df[df['State'] == selected_state]
        fig = px.scatter_map(state_df, lat='Latitude', lon='Longitude', zoom=5.5, map_style="carto-positron", size=primary,
                             color=secondary, width=1500, height=560,hover_name="District")
        # to plot plotly in streamlit
        st.plotly_chart(fig, use_container_width=True)
