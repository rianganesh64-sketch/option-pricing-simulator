import streamlit as st
from ui_components.navbar import display_nav_bar

def display_resources():
    display_nav_bar("Home", "Tutorial", "Simulator", "Quiz", "Math")
    st.space("small")
    st.title("Resources", text_alignment="center")
    st.write("Resources content goes here.")
    st.write("possible resource content" \
    "- law of large numbers" \
    "geometric brownian motion" \
    "monte carlo" \
    "history on black scholes" \
    "quantguild")
    st.header("possible future improvement: have definitions pop-up on anything that is confusing, to prevent unnecessary in app explainations")