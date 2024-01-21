import streamlit as st
import pandas as pd
import io
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

def eda():
    
    df = pd.read_csv('new_laptop.csv', index_col=0)
    
    submenu = ['Descriptive', 'Visualization']
    choice = st.sidebar.selectbox('Submenu', submenu)

    if choice == 'Descriptive':
        col1, col2 = st.columns(2)

        with col1:
            st.subheader('Descriptive statistic')
            st.dataframe(df.describe())
        with col2:
            st.subheader('Data Types')
            st.dataframe(df.dtypes)
        with col1:
            st.subheader('Data Information')
            buffer = io.StringIO()
            df.info(buf=buffer)
            s = buffer.getvalue()
            st.text(s) 
            
        with col2:
            with st.expander('Data Visualisation'):
                st.dataframe(df['TypeOfLaptop'].value_counts())
    else:
        with st.expander('Data Visualization'):
            choose = st.selectbox('Choose a plot to view', ['Type of Laptop', 'Screen Resolution', 'Cpu', 'Gpu', 'Operating System'])
            if choose == 'Type of Laptop':
                a = px.bar(df, x='TypeOfLaptop', width=600, height=400, color='TypeOfLaptop')
                st.plotly_chart(a)
            elif choose == 'Screen Resolution':
                b = px.bar(df, x='ScreenResolution', width=600, height=400, color='ScreenResolution')
                st.plotly_chart(b)
            elif choose == 'Cpu':
                c = px.bar(df, x='Cpu',width=600, height=400, color='Cpu')
                st.plotly_chart(c)
            elif choose == 'Gpu':
                d = px.bar(df, x='Gpu',width=600, height=400, color='Gpu')
                st.plotly_chart(d)
            elif choose == 'Operating System':
                e = px.bar(df, x='OpSys', width=600, height=400, color='OpSys')
                st.plotly_chart(e)    