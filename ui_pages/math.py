import streamlit as st
from ui_components.navbar import display_nav_bar

def display_math():
    display_nav_bar("Home", "Tutorial", "Simulator", "Quiz", "Resources")
    st.title("Math", text_alignment="center")
    st.space("medium")
    col1, col2, col3 = st.columns(3, border=True)
    with col1:
        st.write("black scholes")
    with col2:
        st.write("gbm")
    with col3:
        st.write("monte carlo")


    st.write("try to model after interactiveness of brilliant.com")
