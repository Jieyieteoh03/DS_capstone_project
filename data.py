import streamlit as st
import pandas as pd
import io
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

def data():
    df = pd.read_csv('train.csv', index_col=0)
    
    
    