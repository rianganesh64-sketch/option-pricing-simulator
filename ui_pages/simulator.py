import streamlit as st

def display_simulator():
    st.markdown(
    """
    <style>
        .vertical-divider {
            border-left: 2px solid #fafafa;
            height: 450px;
            margin: 0 auto;
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
    st.space("medium")
    st.title("Welcome to the Simulator!", text_alignment="center")
    st.space("medium")
    input_col, divider_col, output_col = st.columns([1, 0.05, 2.5])
    with input_col:
        st.header("Inputs", text_alignment="center")
        st.space("medium")
        st.write("Stock price input will go here")
        st.write("strike price input goes here")
        st.write("volatility slider goes here")
        st.space("large")
        st.write("run buttons go here")
    with divider_col:
      st.html(
          """
          <div class="vertical-divider"></div>
          """)
    with output_col:
        st.header("Outputs", text_alignment="center")
        st.space("medium")
        st.header("GBM graphs go here", text_alignment="center")
        st.space("medium")
        st.write("black-scholes price goes here: (formatting functions used)")
        st.write("monte_carlo price goes here: (formatting functions used)")