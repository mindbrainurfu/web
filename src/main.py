import streamlit as st
import pandas as pd
import numpy as np

st.title('mindbrain')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')


st.audio_input("Записать аудио:")
st.markdown("<hr>", unsafe_allow_html=True)
st.subheader("или:")
uploaded_file = st.file_uploader("Загрузить аудио:", type=['mp3','wav'])






