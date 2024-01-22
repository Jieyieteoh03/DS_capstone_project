import streamlit as st
from PIL import Image

def ml():
    st.title('Machine learning')
    st.write('Accuracy:')
    img = Image.open('ml 1.png')
    st.image(img)
    st.write('Traning and testing model for Mean Squared Error:')
    img = Image.open('ml 2.png')
    st.image(img)
    st.write('Traning and testing model for Loss:')
    img = Image.open('ml 3.png')
    st.image(img)
    st.write('Actual and predicted:')
    img = Image.open('ml 4.png')
    st.image(img)
    