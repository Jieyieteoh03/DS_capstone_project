import streamlit as st
from PIL import Image


def methodology():
    st.subheader('Methodology')
    st.write('Dataset: https://www.kaggle.com/datasets/sagaraiarchitect/laptop-price-explorer-the-ml-model/data')
    st.write('Framework used: Jupyter ')
    st.write('Libraries used:')
    img = Image.open('tools.png')
    st.image(img)