import streamlit as st
from src.black_scholes import black_scholes_price
from src.monte_carlo import monte_carlo_price
from src.utils import format_currency, absolute_error, percent_error, measure_runtime, format_percent
def display_simulator():
    st.markdown(
    """
    <style>
        .vertical-divider {
            border-left: 2px solid #0e1117; 
            height: 1000px;
            margin: 0 auto;
        }
    </style>
    """,
    unsafe_allow_html=True
    )
    if "bs_price" not in st.session_state:
        st.session_state.bs_price = None
    
    if "mc_price" not in st.session_state:
        st.session_state.mc_price = None
    if "mc_runtime" not in st.session_state:
        st.session_state.mc_runtime = None
    #temporarily blacking out border to see how it looks, will change back if necessary
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
        with st.form("pricing form"):
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
            num_simulations = st.slider("Number of Monte-carlo simulations", 100, 100000, step = 100)
            st.write("Entered Number of Simulations:", num_simulations)
            st.caption("Lower simulation counts usually create noisier, less stable estimates. More simulations can improve accuracy, but they also take longer to run. Try changing this value and see what happens!", text_alignment="center")
            st.space("xxsmall")
            selected_option = st.radio(
                "Call or Put Option?:",
                ["Call", "Put"],
                horizontal=True
            )
            st.space("xxsmall")
            submitted_bs = st.form_submit_button("Run Black Scholes")
            submitted_mc = st.form_submit_button("Run Monte Carlo Simulation")
    
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
        if submitted_bs==True:
            S = stock_input
            K = strike_input
            T = exp_time/12
            r = risk_free_rate_input/100
            sigma = volatility/100
            option_type = selected_option.strip().lower()
            bs_price = black_scholes_price(S, K, T, r, sigma, option_type)
            st.session_state.bs_price = bs_price
        st.space("medium")
        if submitted_mc==True:
            S = stock_input
            K = strike_input
            T = exp_time/12
            r = risk_free_rate_input/100
            sigma = volatility/100
            N = num_simulations
            option_type = selected_option.strip().lower()
            result, execution_time = measure_runtime(
                monte_carlo_price, S, K, T, r, sigma, N, option_type)
            st.session_state.mc_price = result
            st.session_state.mc_runtime = round(execution_time, 6)
        if st.session_state.bs_price is not None:
            st.subheader(f"Option Price Calculated by Black-Scholes: {format_currency(st.session_state.bs_price)}", text_alignment="left")
        if st.session_state.mc_price is not None:
            st.subheader(f"Option Price Calculated by Monte Carlo Simulation: {format_currency(st.session_state.mc_price)}", text_alignment="left")
            st.caption(f"Monte Carlo Simulation Runtime: ~{st.session_state.mc_runtime} secs")
        if st.session_state.bs_price is not None and st.session_state.mc_price is not None:
            S = stock_input
            K = strike_input
            T = exp_time/12
            r = risk_free_rate_input/100
            sigma = volatility/100
            N = num_simulations
            option_type = selected_option.strip().lower()

            absolute_err = absolute_error(S, K, T, r, sigma, N, option_type)
            st.write(f"Absolute Error: {round(absolute_err, 2)}")
            per_error = percent_error(S, K, T, r, sigma, N, option_type)
            st.write("Percent Error:", format_percent(per_error))