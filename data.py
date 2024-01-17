import streamlit as st
import pandas as pd
import io
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

def data():
    df = pd.read_csv('train.csv', index_col=0)
    
    st.subheader('Data')
    st.dataframe(df)
    
    
    st.subheader('Descriptive statistic')
    st.dataframe(df.describe())
    
    col1,col2 = st.columns(2)
    
    with col1:
        st.subheader('Data types')
        st.dataframe(df.dtypes)
    with col2:
        st.subheader('Data information')
        buffer = io.StringIO()
        df.info(buf=buffer)
        s = buffer.getvalue()
        st.text(s)
        
    