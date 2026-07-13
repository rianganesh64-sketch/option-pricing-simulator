
import streamlit as st

def display_nav_bar(page1, page2, page3, page4):
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button(page1, use_container_width=True, type="tertiary"):
            st.session_state.page = page1
            st.rerun()
    with col2:
        if st.button(page2, use_container_width=True, type="tertiary"):
            st.session_state.page = page2
            st.rerun()
    with col3:
        if st.button(page3, use_container_width=True, type="tertiary"):
            st.session_state.page = page3
            st.rerun()
    with col4:
        if st.button(page4, use_container_width=True, type="tertiary"):
            st.session_state.page = page4
            st.rerun()