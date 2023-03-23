import streamlit as st
import random

st.title('random picture')

pic_num = random.randint(1, 3)
pic_url = ""

st.image(pic_url)

