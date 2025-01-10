import streamlit as st
import pandas as pd
import numpy as np

st.title('mindbrain')


st.audio_input("Записать аудио:")
st.markdown("<hr>", unsafe_allow_html=True)
st.subheader("или:")
uploaded_file = st.file_uploader("Загрузить аудио:", type=['mp3','wav'])






