import streamlit as st
import librosa

mp3 = 'TEST18.mp3'
loaded = librosa.load(mp3)
st.sidebar.audio(mp3)
st.success('success')