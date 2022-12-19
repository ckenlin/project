import streamlit as st
from PIL import Image
year_list={'2022':{'抒情歌曲','流行歌曲'},'2021':{'抒情歌曲','流行歌曲'},'2020':{'抒情歌曲','流行歌曲'},'2019':{'抒情歌曲','流行歌曲'},'2018':{'抒情歌曲','流行歌曲'}}
option_year=st.sidebar.selectbox("選擇年度",year_list)
option_musiclist=st.sidebar.selectbox("選擇年度",year_list[option_year])  
