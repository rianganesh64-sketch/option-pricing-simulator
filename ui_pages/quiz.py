import streamlit as st
import pandas as pd
import math
from pathlib import Path
from src.utils import format_currency, format_percent
from ui_components.navbar import display_nav_bar
from src.black_scholes import black_scholes_price
from src.monte_carlo import monte_carlo_price


CSV_PATH = Path("data/real_world_option_quiz_scenarios_true_history.csv")
@st.cache_data
def load_quiz_data():
    return pd.read_csv(CSV_PATH)

def display_quiz():
    display_nav_bar("Home", "Tutorial", "Simulator", "Resources")
    st.space("small")
    st.title("Quiz", text_alignment="center")
    st.markdown("### Test your knowledge with real world scenarios!", text_alignment="center")

    quiz_df = load_quiz_data()

    if "quiz_indices" not in st.session_state:
        st.session_state.quiz_indices = quiz_df.sample(5).index.tolist()
    if "quiz_position" not in st.session_state:
        st.session_state.quiz_position = 0
    if "bank_value" not in st.session_state:
        st.session_state.bank_value = 10000
    if "bs_price" not in st.session_state:
        st.session_state.bs_price = None
    if "mc_price" not in st.session_state:
        st.session_state.mc_price = None
    if "quiz_submitted" not in st.session_state:
        st.session_state.quiz_submitted = False
    if "last_action" not in st.session_state:
        st.session_state.last_action = None # Tracks take or skip
    if "chosen_contracts" not in st.session_state:
        st.session_state.chosen_contracts = 0

    def display_quiz_scenario(scenario):
        quiz_container = st.container(border=True)
        with quiz_container:
            header_container = st.container(border=True)
            with header_container:
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.markdown(f"Bank Balance: {format_currency(st.session_state.bank_value)}", text_alignment="center")
                with col2:
                    st.markdown(f"Question: {(st.session_state.quiz_position) + 1} of {len(st.session_state.quiz_indices)}", text_alignment="center")
                with col3:
                    st.markdown(f"Difficulty: {scenario["difficulty"]}", text_alignment="center")
                with col4:
                    st.markdown(f"Category: {scenario["category"]}", text_alignment="center")
            st.title(f"{scenario["title"]} ({scenario["event_date"]})", text_alignment="center")
            st.markdown(f"##### {scenario["pre_decision_context"]}", text_alignment="center")
            st.space("small")
            input_col, decision_col = st.columns([1.2, 2.5], border=True)
            with input_col:
                st.header("Mini-Simulator", text_alignment="center")
                st.space("xxsmall")
                left_col, right_col = st.columns(2, border=False)
                with left_col:
                    stock_input = st.number_input(
                        "Scenario Stock Price:", value = scenario["stock_price"]
                    )
                    exp_time = st.slider("Scenario Time Until Expiry (Months):", 1, 6, value=scenario["time_to_expiration_months"])
                    risk_free_rate_input = st.slider("Scenario Risk-free Rate (%):", 3.5, 5.5, step=0.25, value=scenario["risk_free_rate_percent"])
                with right_col:
                    strike_input = st.number_input(
                        "Scenario Strike Price:", value = scenario["strike_price"]
                    )
                    volatility = st.slider("Scenario Stock Volatity (%):", 1, 200, value = scenario["volatility_percent"])
                    num_simulations = st.slider("Number of Monte-carlo Simulations", 100, 10000, step=100)
                call_put_container = st.container(horizontal_alignment="center")
                with call_put_container:
                    if scenario["option_type"] == "Call":
                        chosen_index = 0
                    else:
                        chosen_index =  1
                    selected_option = st.radio(
                        "Call or Put Option:",
                             ["Call", "Put"],
                             index = chosen_index,
                    horizontal=True)
                bs_col, mc_col = st.columns(2)
                with bs_col:
                    if st.button("Run Black Scholes", use_container_width=True):
                        exp_time = exp_time/12
                        risk_free_rate_input = risk_free_rate_input/100
                        volatility = volatility/100
                        option_type = selected_option.strip().lower()
                        st.session_state.bs_price = black_scholes_price(stock_input, strike_input, exp_time, risk_free_rate_input, volatility, option_type)
 
                with mc_col:
                    if st.button("Run Monte-Carlo Simulation", use_container_width=True):
                        exp_time = exp_time/12
                        risk_free_rate_input = risk_free_rate_input/100
                        volatility = volatility/100
                        option_type = selected_option.strip().lower()
                        st.session_state.mc_price = monte_carlo_price(stock_input, strike_input, exp_time, risk_free_rate_input, volatility, num_simulations, option_type)
                left_display_col, right_display_col = st.columns(2)
                with right_display_col:
                    if st.session_state.mc_price is not None:
                                st.markdown(format_currency(st.session_state.mc_price), text_alignment="center")
                with left_display_col:
                    if st.session_state.bs_price is not None:
                                st.markdown(format_currency(st.session_state.bs_price), text_alignment="center")
            with decision_col:
                left_col, right_col = st.columns([1, 2.5])
                with left_col:
                    st.markdown("### Option Specifications:", text_alignment="center")
                    st.space("small")
                    st.markdown(f"Stock Price: {format_currency(scenario["stock_price"])}", text_alignment="center")
                    st.space("xxsmall")
                    st.markdown(f"Strike Price: {format_currency(scenario["strike_price"])}", text_alignment="center")
                    st.space("xxsmall")
                    st.markdown(f"Time Till Expiry (Months): {scenario["time_to_expiration_months"]}", text_alignment="center")
                    st.space("xxsmall")
                    st.markdown(f"Volatility: {format_percent(scenario["volatility_percent"])}", text_alignment="center")
                    st.space("xxsmall")
                    st.markdown(f"Risk Free Rate: {format_percent(scenario["risk_free_rate_percent"])}", text_alignment="center")
                    st.space("xxsmall")
                    st.markdown(f"Option Type: {scenario["option_type"]}", text_alignment="center")
                    st.space("large")
                with right_col:
                    st.markdown("### Your Decision:", text_alignment="center")
                    st.markdown(f"##### {scenario["setup"]}", text_alignment="center")
                    st.markdown(f"#### **Option Price: {scenario["market_option_price"]}**", text_alignment="center")
                    take_col, skip_col = st.columns(2, border=True)
                    with take_col:
                        st.subheader("Take Option", text_alignment="center")
                        amount_contracts = st.slider("How Many Contracts: ", 1, (math.floor(st.session_state.bank_value / (100 * scenario["market_option_price"]))))
                        st.write("Number of Options Contracts Chosen: ", amount_contracts)
                        st.write(f"Estimated Cost: {format_currency(100 * scenario["market_option_price"] * amount_contracts)}")
                        st.write(f"Remaining Bank Balance: {format_currency(st.session_state.bank_value - (100 * scenario["market_option_price"] * amount_contracts))}")  
                    with skip_col:
                        st.subheader("Skip Trade", text_alignment="center")
                        st.markdown("Doesn't seem right? You don't have to trade!", text_alignment="center")
                    btn_1, btn_2 = st.columns(2)
                    with btn_1:
                        confirm_container = st.container(horizontal_alignment="center")
                        with confirm_container:
                            if st.button("Confirm Trade?", use_container_width=True, type="primary"):
                                st.session_state.last_action = "take"
                                st.session_state.chosen_contracts = amount_contracts
                                st.session_state.quiz_submitted = True
                                st.rerun()
                    with btn_2:
                        skip_container = st.container(horizontal_alignment="center")
                        with skip_container:
                            if st.button("Skip Trade?", use_container_width=True,  type="secondary"):
                                st.session_state.last_action = "skip"
                                st.session_state.chosen_contracts = 0
                                st.session_state.quiz_submitted = True
                                st.rerun()
            st.caption(f"#### Your bank is at **{format_currency(st.session_state.bank_value)}**. Run the mini-simulator, compare its estimate with the market option price, then decide whether to take this option or skip it. If you take it, choose how much of your bank to invest. Each option contract controls 100 shares of the stock.", text_alignment="center")
    def display_summary_scene(scenario):
        summary_container = st.container(border=True)
        with summary_container:
            if st.session_state.last_action == "skip":
                st.title("You Skipped:", text_alignment="center")
                # Temporary debug line to see what columns actually exist
                st.write("Available columns:", list(scenario.keys()))
            else:
                st.title("You Traded:", text_alignment = "center")
                st.subheader(f"Bought: {st.session_state.chosen_contracts} contracts", text_alignment="center")
                st.markdown(f"#### What Happened in Real Life?", text_alignment="center")
                st.markdown(f"#### {scenario["post_event_outcome"]}", text_alignment="center")
                st.space("small")
                # Temporary debug line to see what columns actually exist
                st.write("Available columns:", list(scenario.keys()))
                # if scenario["expiration_status"] == "Out-of-the-Money":
                #     st.header(":red[Unprofitable]")
                # elif scenario["expiration_status"] == "In-the-Money":
                #     st.header(":green[Profitable!]")








                






        
    if st.session_state.quiz_position >= 5:
        st.write("You finished")
        #display_final_screen()
    else:
        scenario_index = st.session_state.quiz_indices[st.session_state.quiz_position]
        current_scenario = quiz_df.loc[scenario_index]

        if st.session_state.quiz_submitted:
            display_summary_scene(current_scenario)
        else:
            display_quiz_scenario(current_scenario)
    

    # st.write(f"Loaded {len(quiz_df)} scenarios.")
    # st.write(quiz_df.iloc[0]["title"])



    # if st.session_state.quiz_position >= 5:
    #     display_final_screen()

    # else:
    #     scenario_index = st.session_state.quiz_indices[st.session_state.quiz_position]
    #     current_scenario = quiz.df.loc[scenario_index]
    #     display_quiz_scenario(scenario)

    # def display_quiz_scenario(scenario):
        
    # def display_final_screen():
    #     card_container = st.container(border=True)
    #     with card_container:
    #             if st.session_state.bank > 10000:
    #                 st.header("Congratulations!", text_alignment="center")
    #                 st.space("small")
    #                 st.subheader(f"Final Balance: {format_currency(st.session_state.bank)}", text_alignment="center")
    #                 st.markdown(f"Your options pricing knowledge made you: {format_currency(st.session_state.bank - 10000)}", text_alignment="center")
    #             again_col, resources_col = st.columns(2)
    #             with again_col:
    #                 with st.container(horizontal_alignment="center"):
    #                     if st.button("Play Again!", use_container_width=True):
    #                             st.session_state.quiz_indices = quiz_df.sample(5).index.tolist()
    #                             st.session_state.quiz_position = 0
    #                             st.session_state.bank = 10000
    #                             st.session_state.quiz_answered = False
    #                             st.rerun()
    #             with resources_col:
    #                 with st.container(horizontal_alignment="center"):
    #                     if st.button("Go to Resources!", use_container_width=True):
    #                         st.session_state.quiz_indices = quiz_df.sample(5).index.tolist()
    #                         st.session_state.quiz_position = 0
    #                         st.session_state.bank = 10000
    #                         st.session_state.quiz_answered = False
    #                         st.session_state.page = "Resources"
    #                         st.rerun()
    #             if st.session_state.bank <= 10000:
    #                 st.header("Great Effort!", text_alignment="center")
    #                 st.space("small")
    #                 st.subheader(f"Final Balance: {format_currency(st.session_state.bank)}", text_alignment="center")

                        




#         1. Load CSV
# 2. Initialize quiz round: choose 5 scenarios
# 3. If quiz_position >= 5:
#        show final balance
#    Else:
#        show current scenario
# 4. User chooses take or skip
# 5. If take, user chooses investment amount
# 6. Reveal outcome and update bank
# 7. User clicks next scenario
# 8. After 5 questions, show final result

# Step 1: Load CSV successfully
# Step 2: Display the first scenario from the CSV
# Step 3: Add quiz_position so you can move through scenarios
# Step 4: Limit one quiz to 5 selected scenarios
# Step 5: Add bank balance
# Step 6: Add take/skip decision
# Step 7: Add final balance screen after 5 questions


# CSV_PATH = Path("data/real_world_option_quiz_scenarios.csv")

# @st.cache_data
# def load_quiz_data():
#     return pd.read_csv(CSV_PATH)

#     quiz_df = load_quiz_data()
    
#     if "quiz_indices" not in st.session_state:
#         st.session_state.quiz_indices = quiz_df.sample(5).index.tolist()
    
#     if "quiz_position" not in st.session_state:
#         st.session_state.quiz_position = 0

#     if "bank" not in st.session_state:
#         st.session_state.bank = 10000

#     if "quiz_answered" not in st.session_state:
#         st.session_state.quiz_answered = False