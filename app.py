import streamlit as st
from ui_components.navbar import display_nav_bar

from ui_pages.tutorial import display_tutorial
from ui_pages.simulator import display_simulator
from ui_pages.quiz import display_quiz
from ui_pages.resources import display_resources

st.set_page_config(layout="wide")

if "page" not in st.session_state:
    st.session_state.page = "Home"



def display_main():
    st.title("Welcome to Option-Pricing-Simulator", text_alignment="center")
    col1, col2 = st.columns(2)
    col1.header("Rian Ganesh", text_alignment="center")
    col2.header("Github:", text_alignment="center")
    col2.markdown("https://github.com/rianganesh64-sketch", text_alignment="center")

    st.space("medium")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("Tutorial"):
            st.session_state.page = "Tutorial"
            st.rerun()
    with col2:
        if st.button("Simulator"):
            st.session_state.page = "Simulator"
            st.rerun()
    with col3:
        if st.button("Quiz"):
            st.session_state.page = "Quiz"
            st.rerun()
    with col4:
        if st.button("Resources"):
            st.session_state.page = "Resources"
            st.rerun()

if st.session_state.page == "Home":
    display_main()
elif st.session_state.page == "Tutorial":
    display_tutorial()

elif st.session_state.page == "Simulator":
    display_simulator()

elif st.session_state.page == "Quiz":
    display_quiz()

elif st.session_state.page == "Resources":
    display_resources()