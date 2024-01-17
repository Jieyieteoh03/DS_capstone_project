import streamlit as st
from PIL import Image
from data import data
# from objective import objective

def main():
    st.title('Hate Speech and Offensive Language Detection')
    menu = ['Home', 'Objective', 'Data']
    choice = st.sidebar.selectbox('Menu', menu)
    if choice == 'Home':
        img = Image.open('twitter image.jpg')
        st.image(img)
    
    # elif choice == 'Objective':
    #     objective()
        
    elif choice == 'Data':
        data()
        
main()