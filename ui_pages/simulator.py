import streamlit as st

def display_simulator():
    st.markdown(
    """
    <style>
        .vertical-divider {
            border-left: 2px solid #fafafa;
            height: 1000px;
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
    input_col, divider_col, output_col = st.columns([1.2, 0.05, 2.5])
    with input_col:
        st.header("Inputs", text_alignment="center")
        st.space("medium")
        stock_input = st.number_input(
            "Enter Current Stock Price:", min_value = 0.01, value=100.00)
        st.write("Entered Stock Price: ", stock_input)
        st.space("xxsmall")
        strike_input = st.number_input(
            "Enter Option Strike Price:", min_value = 0.01, value=110.00
        )
        st.write("Entered Strike Price:", strike_input)
        st.space("xxsmall")
        exp_time = st.slider("How long until the Option expires? (months)", 1, 60, value=12)
        st.write("Entered Time Till Expiration:", exp_time)
        st.space("xxsmall")
        volatility = st.slider("Stock Volatility (%):", 0, 100, value=15)
        st.write("Entered Stock Volatility:", volatility,"%")
        st.space("xxsmall")
        risk_free_rate_input = st.slider("Risk-free Rate (%)", 0.00, 15.00, step=0.25)
        st.write("Entered Risk-free rate:", risk_free_rate_input,"%")
        st.space("xxsmall")
        num_simulations = st.slider("Number of Monte-carlo simulations", 10, 10000, step = 50)
        st.write("Entered Number of Simulations:", num_simulations)
        st.caption("Lower simulation counts usually create noisier, less stable estimates. More simulations can improve accuracy, but they also take longer to run. Try changing this value and see what happens!", text_alignment="center")
        st.space("xxsmall")
        option_type = st.radio(
            "Call or Put Option?:",
            ["**Call**", "**Put**"],
            horizontal=True
        )
        st.space("xxsmall")
        run_bs = st.button("Run Black-Scholes", use_container_width=True)
        run_mc = st.button("Run Monte Carlo Simulation", use_container_width=True)

        if run_bs:
            st.write("Black-scholes button clicked")
        if run_mc:
            st.write("Monte-carlo button clicked")
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

