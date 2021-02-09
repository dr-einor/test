import streamlit as st
import librosa

if librosa.load('TEST18.mp3'):
    st.success('success')