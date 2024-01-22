import streamlit as st
import pandas as pd
import io
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

def data():    
    df1 = pd.read_csv('laptops.csv', index_col=None)
    df = pd.read_csv('new_laptop.csv', index_col=None)
   
    st.subheader('Before Data Cleaning')
    st.dataframe(df1)
    
    st.subheader('After Data Cleaning')
    st.dataframe(df)
        
    