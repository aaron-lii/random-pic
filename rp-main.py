import streamlit as st
import random
import requests

st.title('random picture')

def get_pic(url):
    r = requests.get(url, timeout=5)
    return r.content


pic_dir_num = random.randint(0, 1)
if pic_dir_num == 0:
    pic_num = random.randint(1, 1)
    pic_url = "https://github.com/aaron-lii/random-pic/raw/main/pics/" + str(pic_num) + ".png"
else:
    pic_num = random.randint(1, 2)
    pic_url = "https://github.com/aaron-lii/random-pic/raw/main/gifs/" + str(pic_num) + ".gif"


st.image(get_pic(pic_url))

