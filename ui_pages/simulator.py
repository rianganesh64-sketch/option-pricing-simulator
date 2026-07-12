import streamlit as st
import matplotlib.pyplot as plt
from src.black_scholes import black_scholes_price
from src.monte_carlo import monte_carlo_price
from src.utils import format_currency, absolute_error, percent_error, measure_runtime, format_percent
from src.gbm import generate_gbm_paths
def display_simulator():
    st.markdown(
    """
    <style>
        .vertical-divider {
            border-left: 2px solid #fafafa; 
            height: 1400px;
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
    if "gbm_paths" not in st.session_state:
        st.session_state.gbm_paths = None
    col1, col2, col3, col4 = st.columns(4, border=False)
    with col1:
        if st.button("Home", use_container_width=True, type="tertiary"):
            st.session_state.page = "Home"
            st.rerun()
    with col2:
        if st.button("Tutorial", use_container_width=True, type="tertiary"):
            st.session_state.page = "Tutorial"
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
    st.markdown("### Experiment with different option inputs and compare how Black-Scholes and Monte Carlo prices change.", text_alignment="center")
    st.space("small")
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
            volatility = st.slider("Stock Volatility (%):", 0.01, 100.00, value=15.00)
            st.write("Entered Stock Volatility:", volatility,"%")
            st.space("xxsmall")
            risk_free_rate_input = st.slider("Risk-free Rate (%)", 0.00, 15.00, step=0.25)
            st.write("Entered Risk-free rate:", risk_free_rate_input,"%")
            st.space("xxsmall")
            num_simulations = st.slider("Number of Monte-carlo simulations", 100, 100000, step = 100)
            st.write("Entered Number of Simulations:", num_simulations)
            st.caption("Lower simulation counts usually create noisier, less stable estimates. More simulations can improve accuracy, but they also take longer to run. Try changing this value and see what happens!", text_alignment="center")
            st.space("xxsmall")
            num_paths = st.slider("How many GBM Paths to Generate?", 1, 5, value=10)
            st.write("Number of Displayed GBM Paths:", num_paths)
            st.space("xxsmall")
            selected_option = st.radio(
                "Call or Put Option?:",
                ["Call", "Put"],
                horizontal=True
            )
            st.space("xxsmall")
            submit_bs, submit_mc = st.columns(2)
            with submit_bs:
                submitted_bs = st.button("Run Black Scholes", use_container_width=True)
            with submit_mc:
                submitted_mc = st.button("Run Monte Carlo Simulation", use_container_width=True)
    
    with divider_col:
      st.html(
          """
          <div class="vertical-divider"></div>
          """)
    with output_col:
        st.header("Outputs", text_alignment="center")
        if submitted_bs==False and submitted_mc==False:
            st.space('xxlarge')
            st.subheader("Start changing input values to get started:", text_alignment="center")
            st.space("large")
            st.subheader('Click "Run Black Scholes" or "Run Monte Carlo Simulation" to see the outputs!', text_alignment="center")
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
            num_gbm_paths = num_paths
            num_gbm_steps = max(1, int(252 * T))
            result, execution_time = measure_runtime(
                monte_carlo_price, S, K, T, r, sigma, N, option_type)
            st.session_state.mc_price = result
            st.session_state.mc_runtime = round(execution_time, 6)
            gbm_paths = generate_gbm_paths(S, T, r, sigma, num_gbm_steps, num_gbm_paths)
            st.session_state.gbm_paths = gbm_paths
        if st.session_state.bs_price is not None:
            st.subheader(f"Black-Scholes Option Price: {format_currency(st.session_state.bs_price)}", text_alignment="center")
        if st.session_state.mc_price is not None:
            st.subheader(f"Monte Carlo Option Price: {format_currency(st.session_state.mc_price)}", text_alignment="center")
            st.caption(f"Monte Carlo Simulation Runtime: ~{st.session_state.mc_runtime} secs", text_alignment="center")
        if st.session_state.bs_price is not None and st.session_state.mc_price is not None:
            S = stock_input
            K = strike_input
            T = exp_time/12
            r = risk_free_rate_input/100
            sigma = volatility/100
            N = num_simulations
            option_type = selected_option.strip().lower()
            absolute_err = absolute_error(round(st.session_state.bs_price, 2), round(st.session_state.mc_price, 2))
            per_error = percent_error(round(st.session_state.bs_price, 2), round(st.session_state.mc_price, 2))
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"Absolute Error (Difference Between Prices): ${round(absolute_err, 2)}", text_alignment="right")
            with col2:
                if st.session_state.bs_price == 0.00:
                    st.markdown("Percent Error: Undefined (Black-Scholes Price is 0)", text_alignment="left")
                else:
                    st.markdown(f"Percent Error: {format_percent(per_error)}", text_alignment="left")
            st.space("medium")
            if st.session_state.gbm_paths is not None:
                fig, ax = plt.subplots(figsize = (5,2.9166))
                
                for path in st.session_state.gbm_paths:
                    ax.plot(path)
                
                ax.set_title("Simulated Stock GBM Paths")
                ax.set_xlabel("Time (Trading Days)")
                ax.set_ylabel("Stock Price")
                st.pyplot(fig, use_container_width=True)
                st.caption("This graph visualizes potential prices of the underlying stock using Geometric Brownian Motion. A Monte Carlo simulation can run a lot of these to get an average future stock price. It uses this price to calculate the value of an option.", text_alignment="center")
