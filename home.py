import streamlit as st
from PIL import Image
from data import data
from eda import eda
from objective import objective
from methodology import methodology
from ml import ml

def main():
    st.title('Laptop Price')
    st.subheader('Name: Teoh Jie Yie')
    menu = ['Home', 'Objective', 'Methodology','Data Cleaning', 'EDA', 'ML']
    choice = st.sidebar.selectbox('Menu', menu)
    if choice == 'Home':
        img = Image.open('laptop.jpg')
        st.image(img)
    
    elif choice == 'Objective':
        objective()
        
    elif choice == 'Methodology':
        methodology()
        
    elif choice == 'ML':
        ml()
        
    elif choice == 'Data Cleaning':
        data()
    
    elif choice == 'EDA':
        eda()
    
main()