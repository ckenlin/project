import streamlit as st
from PIL import Image
year_list={'2022','2021','2020','2019','2018'}
option_year=st.sidebar.selectbox("選擇年度",year_list)
type_list={'抒情歌曲','流行歌曲'}
option_musiclist=st.sidebar.selectbox("選擇年度",type_list)  
music_list={'bb','cc'}
