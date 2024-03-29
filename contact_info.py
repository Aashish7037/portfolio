import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

def create_streamlit_content():

    load_css()

    st.write("[![Star](https://img.shields.io/github/stars/dataprofessor/links.svg?logo=github&style=social)](https://github.com/Aashish7037)")

    col1, col2, col3 = st.columns(3)
    col2.image(Image.open('dp.png'))

    st.header('Aashish Kumar, B.Tech')

    st.info('Python developer, backend developer with a deep interest in new tecnologies')
    icon_size = 20

    st_button('linkedin', 'https://www.linkedin.com/in/aashish-choudhary-695a541b1/', 'linkedin', icon_size)

if __name__ == "__main__":
    create_streamlit_content()
