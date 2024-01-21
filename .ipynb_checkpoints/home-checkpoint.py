import streamlit as st
from PIL import Image
from data import data
from eda import eda
# from objective import objective

def main():
    st.title('Laptop Price')
    menu = ['Home', 'Objective', 'Data Cleaning', 'EDA']
    choice = st.sidebar.selectbox('Menu', menu)
    if choice == 'Home':
        img = Image.open('laptop.jpg')
        st.image(img)
    
    # elif choice == 'Objective':
    #     objective()
        
    elif choice == 'Data Cleaning':
        data()
    
    elif choice == 'EDA':
        eda()
main()