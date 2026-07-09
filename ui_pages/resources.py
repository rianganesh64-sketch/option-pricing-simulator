import streamlit as st

def display_resources():
    st.set_page_config(layout="wide")
    st.set_page_config(layout="wide")
    st.markdown(
    """
    <style>
        div[data-testid="stHorizontalBlock"] {
            background-color: #4a76fd;
            padding: 12px 30px;
            border-radius: 0px;
        }

        div[data-testid="stButton"] > button {
            color: white;
            font-weight: 600;
        }

        div[data-testid="stButton"] > button:hover {
            color: #BBDEFB;
        }
    </style>
    """,
    unsafe_allow_html=True
    )
    col1, col2, col3, col4 = st.columns(4, border=False)
    with col1:
        if st.button("Tutorial", use_container_width=True, type="tertiary"):
            st.session_state.page = "Tutorial"
            st.rerun()
    with col2:
        if st.button("Simulator", use_container_width=True, type="tertiary"):
            st.session_state.page = "Simulator"
            st.rerun()
    with col3:
        if st.button("Quiz", use_container_width=True, type="tertiary"):
            st.session_state.page = "Quiz"
            st.rerun()
    with col4:
        if st.button("Resources", use_container_width=True, type="tertiary"):
            st.session_state.page = "Resources"
            st.rerun()
    st.title("resources")
    st.write("Resources content goes here.")