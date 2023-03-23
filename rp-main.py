import streamlit as st
import random

st.title('random picture')

pic_dir_num = random.randint(0, 1)
if pic_dir_num == 0:
    pic_num = random.randint(1, 1)
    pic_url = "https://github.com/aaron-lii/random-pic/raw/main/pics/" + str(pic_num) + ".png"
else:
    pic_num = random.randint(1, 2)
    pic_url = "https://github.com/aaron-lii/random-pic/raw/main/gifs/" + str(pic_num) + ".gif"


st.image(pic_url)

