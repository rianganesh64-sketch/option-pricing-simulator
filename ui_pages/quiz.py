import streamlit as st
import pandas as pd
import math
from pathlib import Path
from src.utils import format_currency, format_percent
from ui_components.navbar import display_nav_bar
from src.black_scholes import black_scholes_price
from src.monte_carlo import monte_carlo_price


CSV_PATH = Path("data/rebalanced_options_quiz_scenarios.csv")
@st.cache_data
def load_quiz_data():
    return pd.read_csv(CSV_PATH)

def display_quiz():
    display_nav_bar("Home", "Tutorial", "Simulator", "Math", "Resources")
    # st.space("small")
    # st.title("Quiz", text_alignment="center")
    # st.markdown("### Test your knowledge with real world scenarios!", text_alignment="center")

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
    if "quiz_history" not in st.session_state:
        st.session_state.quiz_history = [{} for _ in range(5)]

    def display_quiz_scenario(scenario):
        st.space("small")
        st.title("Quiz", text_alignment="center")
        st.markdown("### Test your knowledge with real world scenarios!", text_alignment="center")
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
                    st.markdown(f"#### Stock Price: {format_currency(scenario["stock_price"])}", text_alignment="center")
                    st.space("xxsmall")
                    st.markdown(f"#### Strike Price: {format_currency(scenario["strike_price"])}", text_alignment="center")
                    st.space("xxsmall")
                    st.markdown(f"#### Time Till Expiry (Months): {scenario["time_to_expiration_months"]}", text_alignment="center")
                    st.space("xxsmall")
                    st.markdown(f"#### Volatility: {format_percent(scenario["volatility_percent"])}", text_alignment="center")
                    st.space("xxsmall")
                    st.markdown(f"#### Risk Free Rate: {format_percent(scenario["risk_free_rate_percent"])}", text_alignment="center")
                    st.space("xxsmall")
                    st.markdown(f"#### Option Type: {scenario["option_type"]}", text_alignment="center")
                    st.space("medium")
                with right_col:
                    st.markdown("### Your Decision:", text_alignment="center")
                    st.markdown(f"##### {scenario["setup"]}", text_alignment="center")
                    st.markdown(f"#### **Option Price: {scenario["market_option_price"]}**", text_alignment="center")
                    take_col, skip_col = st.columns(2, border=True)
                    with take_col:
                        st.subheader("Take Option", text_alignment="center")
                        max_contracts = math.floor(st.session_state.bank_value / (100 * scenario["market_option_price"]))
                        if max_contracts >= 2:
                            amount_contracts = st.slider("How Many Contracts: ", 1, (math.floor(st.session_state.bank_value / (100 * scenario["market_option_price"]))))
                            st.write("Number of Options Contracts Chosen: ", amount_contracts)
                            st.session_state.chosen_contracts = amount_contracts #figure this out, possibly unbound error
                            st.write(f"Estimated Cost: {format_currency(100 * scenario["market_option_price"] * amount_contracts)}")
                            st.write(f"Remaining Bank Balance: {format_currency(st.session_state.bank_value - (100 * scenario["market_option_price"] * amount_contracts))}") 
                        if max_contracts == 1:
                            st.warning("Your bank balance only permits the purchase of exactly **1 contract** for this trade") #find a way for center alignmnet, possibly custom html injection
                            amount_contracts = 1
                            st.write(f"Estimated Cost: {format_currency(100 * scenario["market_option_price"] * amount_contracts)}")
                            st.write(f"Remaining Bank Balance: {format_currency(st.session_state.bank_value - (100 * scenario["market_option_price"] * amount_contracts))}")
                        elif max_contracts < 1:
                            st.error("**Insufficient Funds:** Your bank doesn't permit you to purchase any option contracts")
                            amount_contracts = 0
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

                                premium_cost = scenario["market_option_price"] * st.session_state.chosen_contracts * 100
                                strike = scenario["strike_price"]
                                final_stock_price = scenario["stock_price_at_expiration"]
                                if scenario["expiration_status"] == "Out-of-the-Money":
                                    final_option_worth = 0.0
                                else:
                                    if scenario["option_type"] == "Call":
                                        final_option_worth = max(final_stock_price - strike, 0.0) * st.session_state.chosen_contracts * 100
                                    else:
                                        final_option_worth = max(strike - final_stock_price, 0.0) * st.session_state.chosen_contracts * 100
                                
                                net_profit = final_option_worth - premium_cost
                                st.session_state.bank_value = st.session_state.bank_value + net_profit

                                idx = st.session_state.quiz_position
                                st.session_state.quiz_history[idx] = {
                                    "title": scenario["title"],
                                    "date": scenario["event_date"],
                                    "description": scenario['pre_decision_context'],
                                    "stock_price": scenario["stock_price"],
                                    "strike_price": scenario["strike_price"],
                                    "time_till_expiry": scenario["time_to_expiration_months"],
                                    "volatility": scenario["volatility_percent"],
                                    "risk_free_rate": scenario["risk_free_rate_percent"],
                                    "category": scenario["category"],
                                    "difficulty": scenario["difficulty"],
                                    "option_price": scenario["market_option_price"],
                                    "ticker": scenario["ticker"],
                                    "option_type": scenario["option_type"],
                                    "action": "Trade",
                                    "num_contracts": amount_contracts,
                                    "result": scenario["post_event_outcome"],
                                    "itm_otm": scenario["expiration_status"],
                                    "profit_loss": net_profit,
                                    "ending_bank": st.session_state.bank_value,
                                    "lesson": scenario["lesson"]
                                }
                                st.rerun()
                    with btn_2:
                        skip_container = st.container(horizontal_alignment="center")
                        with skip_container:
                            if st.button("Skip Trade?", use_container_width=True,  type="secondary"):
                                st.session_state.last_action = "skip"
                                st.session_state.chosen_contracts = 0
                                st.session_state.quiz_submitted = True
                                st.session_state.bank_value = st.session_state.bank_value

                                idx = st.session_state.quiz_position
                                st.session_state.quiz_history[idx] = {
                                    "title": scenario["title"],
                                    "date": scenario["event_date"],
                                    "description": scenario['pre_decision_context'],
                                    "stock_price": scenario["stock_price"],
                                    "strike_price": scenario["strike_price"],
                                    "time_till_expiry": scenario["time_to_expiration_months"],
                                    "volatility": scenario["volatility_percent"],
                                    "risk_free_rate": scenario["risk_free_rate_percent"],
                                    "category": scenario["category"],
                                    "difficulty": scenario["difficulty"],
                                    "option_price": scenario["market_option_price"],
                                    "ticker": scenario["ticker"],
                                    "option_type": scenario["option_type"],
                                    "action": "Skip",
                                    "num_contracts": 0,
                                    "result": scenario["post_event_outcome"],
                                    "itm_otm": scenario["option_type"],
                                    "profit_loss": 0,
                                    "ending_bank": st.session_state.bank_value,
                                    "lesson": scenario["lesson"]
                                }
                                st.rerun()
            st.caption(f"#### Your bank is at **{format_currency(st.session_state.bank_value)}**. Run the mini-simulator, compare its estimate with the market option price, then decide whether to take this option or skip it. If you take it, choose how much of your bank to invest. Each option contract controls 100 shares of the stock.", text_alignment="center")

    def display_summary_scene(scenario):
        st.space("small")
        st.title("Quiz", text_alignment="center")
        st.markdown("### Test your knowledge with real world scenarios!", text_alignment="center")
        summary_container = st.container(border=True)
        with summary_container:
            if st.session_state.last_action == "skip":
                if scenario["expiration_status"] == "Out-of-the-Money":
                    st.title("You Skipped: Great Job!", text_alignment="center")
                else:
                    st.title("You Skipped: Are you sure?", text_alignment="center")
                st.markdown(f"#### What Happened in Real Life?", text_alignment="center")
                st.markdown(f"#### {scenario["post_event_outcome"]}", text_alignment="center")
                if scenario["expiration_status"] == "Out-of-the-Money":
                     st.title(":red[Unprofitable]", text_alignment="center")
                elif scenario["expiration_status"] == "In-the-Money":
                     st.title(":green[Profitable!]", text_alignment="center")
                st.header("Lesson From this Trade:", text_alignment="center")
                st.subheader(f"{scenario["lesson"]}", text_alignment="center")
                st.subheader(f"Current Bank Balance: {format_currency(st.session_state.bank_value)}", text_alignment="center")
                button_container = st.container(horizontal_alignment="center")
                with button_container:
                    if st.session_state.quiz_position >= 4:
                        if st.button("Finish!", type="primary"):
                            st.session_state.quiz_position += 1
                            st.session_state.bs_price = None
                            st.session_state.mc_price = None
                            st.session_state.quiz_submitted = False
                            st.session_state.last_action = None
                            st.session_state.chosen_contracts = 0
                            st.rerun()
                    else:
                        if st.button("Next Question!", type="primary"):
                            st.session_state.quiz_position += 1
                            st.session_state.bs_price = None
                            st.session_state.mc_price = None
                            st.session_state.quiz_submitted = False
                            st.session_state.last_action = None
                            st.session_state.chosen_contracts = 0
                            st.rerun()
            else:
                st.title(f"You Traded {st.session_state.chosen_contracts} contracts of {scenario["ticker"]} {scenario["option_type"]} Options", text_alignment = "center")
                st.markdown(f"#### What Happened in Real Life?", text_alignment="center")
                st.markdown(f"#### {scenario["post_event_outcome"]}", text_alignment="center")
                if scenario["expiration_status"] == "Out-of-the-Money":
                     st.title(":red[Unprofitable]", text_alignment="center")
                elif scenario["expiration_status"] == "In-the-Money":
                     st.title(":green[Profitable!]", text_alignment="center")
                st.header("Lesson From this Trade:", text_alignment="center")
                st.subheader(f"{scenario["lesson"]}", text_alignment="center")
                st.space("medium")
                # premium_cost = scenario["market_option_price"] * st.session_state.chosen_contracts * 100
                # strike = scenario["strike_price"]
                # final_stock_price = scenario["stock_price_at_expiration"]
                # if scenario["expiration_status"] == "Out-of-the-Money":
                #     final_option_worth = 0.0
                # else:
                #     if scenario["option_type"] == "Call":
                #         final_option_worth = max(final_stock_price - strike, 0.0) * st.session_state.chosen_contracts * 100
                #     else:
                #         final_option_worth = max(strike - final_stock_price, 0.0) * st.session_state.chosen_contracts * 100
                # st.session_state.bank_value = st.session_state.bank_value - premium_cost + final_option_worth
                st.subheader(f"Current Bank Balance: {format_currency(st.session_state.bank_value)}", text_alignment="center")
                button_container = st.container(horizontal_alignment="center")
                with button_container:
                    if st.session_state.quiz_position >= 4:
                        if st.button("Finish!", type="primary"):
                            st.session_state.quiz_position += 1
                            st.session_state.bs_price = None
                            st.session_state.mc_price = None
                            st.session_state.quiz_submitted = False
                            st.session_state.last_action = None
                            st.session_state.chosen_contracts = 0
                            st.rerun()
                    else:
                        if st.button("Next Question!", type="primary"):
                            st.session_state.quiz_position += 1
                            st.session_state.bs_price = None
                            st.session_state.mc_price = None
                            st.session_state.quiz_submitted = False
                            st.session_state.last_action = None
                            st.session_state.chosen_contracts = 0
                            st.rerun()
                

        
    if st.session_state.quiz_position >= 5:
        st.space("small")
        if st.session_state.bank_value > 10000:
            st.title("Quiz Complete: Congratulations!", text_alignment="center")
            total_profit = st.session_state.bank_value - 10000
            st.header(f"Total Profit: :green[{format_currency(total_profit)}]", text_alignment="center")
            st.header(f"Final Bank Balance: :green[{format_currency(st.session_state.bank_value)}]", text_alignment="center")
            st.subheader("Let's analyze your trades:", text_alignment="center")
            st.space("small")
        elif st.session_state.bank_value < 10000:
            st.title("Quiz Complete: You Learnt a Lot!", text_alignment="center")
            total_profit = 10000 -  st.session_state.bank_value 
            st.header(f"Total Loss: :red[-{format_currency(total_profit)}]", text_alignment="center")
            st.header(f"Final Bank Balance: :red[{format_currency(st.session_state.bank_value)}]", text_alignment="center")
            st.subheader("Let's analyze your trades:", text_alignment="center")
            st.space("small")
        else:
            st.title("Quiz Complete: You Learnt a Lot!", text_alignment="center")
            total_profit = 10000 -  st.session_state.bank_value 
            st.header(f"Total Profit: :grey[{format_currency(total_profit)}]", text_alignment="center")
            st.header(f"Final Bank Balance: :grey[{format_currency(st.session_state.bank_value)}]", text_alignment="center")
            st.subheader("Let's analyze your trades:", text_alignment="center")
            st.space("small")

        for i in range(5):
            trade = st.session_state.quiz_history[i]

            if not trade:
                continue
                
            if trade["profit_loss"] > 0:
                with st.expander(f"Scenario {i+1}: {trade['ticker']} {trade["option_type"]} Option {trade['action']}: :green[+{format_currency(trade["profit_loss"])}]",):
                    st.subheader(f"{trade["title"]} ({trade["date"]})", text_alignment="center")
                    st.markdown(f" ##### {trade["description"]}", text_alignment="center")
                    spec_col, result_col = st.columns([1, 2.5], border=True)
                    with spec_col:
                            st.markdown(f" ##### Option Specifications:", text_alignment="center")
                            st.markdown(f"###### Stock Price: {format_currency(trade["stock_price"])}", text_alignment="center")
                            st.markdown(f"###### Strike Price: {format_currency(trade["strike_price"])}", text_alignment="center")
                            st.markdown(f"###### Time Till Expiry (Months): {trade["time_till_expiry"]}", text_alignment="center")
                            st.markdown(f"###### Volatility: {format_percent(trade["volatility"])}", text_alignment="center")
                            st.markdown(f"###### Risk Free Rate: {format_percent(trade["risk_free_rate"])}", text_alignment="center")
                            st.markdown(f"###### Option Type: {trade["option_type"]}", text_alignment="center")
                    with result_col:
                            st.markdown(f"##### Market Option Price: {format_currency(trade["option_price"])}", text_alignment="center")
                            st.markdown(f"##### Your Decision: {trade["action"]} {trade["num_contracts"]} {trade["option_type"]} Contracts", text_alignment="center")
                            st.markdown(f"##### Result: :green[+{format_currency(trade["profit_loss"])}] ", text_alignment="center")
                            st.markdown(f"{trade["result"]}", text_alignment="center")
                            st.markdown(f"{trade["lesson"]}", text_alignment="center")
                    footer_container = st.container(border=True)
                    with footer_container:
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            st.caption(f"Difficulty: {trade["difficulty"]}", text_alignment="center")
                        with col2:
                            st.caption(f"Bank Balance: {format_currency(trade["ending_bank"])}", text_alignment="center")
                        with col3:
                            st.caption(f"Category: {trade["category"]}", text_alignment="center")
            elif trade["profit_loss"] < 0:
                with st.expander(f"Scenario {i+1}: {trade['ticker']} {trade["option_type"]} Option {trade['action']}: :red[-{format_currency(abs(trade["profit_loss"]))}]"):
                    st.subheader(f"{trade["title"]} ({trade["date"]})", text_alignment="center")
                    st.markdown(f" ##### {trade["description"]}", text_alignment="center")
                    spec_col, result_col = st.columns([1, 2.5], border=True)
                    with spec_col:
                            st.markdown(f" ##### Option Specifications:", text_alignment="center")
                            st.markdown(f"###### Stock Price: {format_currency(trade["stock_price"])}", text_alignment="center")
                            st.markdown(f"###### Strike Price: {format_currency(trade["strike_price"])}", text_alignment="center")
                            st.markdown(f"###### Time Till Expiry (Months): {trade["time_till_expiry"]}", text_alignment="center")
                            st.markdown(f"###### Volatility: {format_percent(trade["volatility"])}", text_alignment="center")
                            st.markdown(f"###### Risk Free Rate: {format_percent(trade["risk_free_rate"])}", text_alignment="center")
                            st.markdown(f"###### Option Type: {trade["option_type"]}", text_alignment="center")
                    with result_col:
                            st.markdown(f"##### Market Option Price: {format_currency(trade["option_price"])}", text_alignment="center")
                            st.markdown(f"##### Your Decision: {trade["action"]} {trade["num_contracts"]} {trade["option_type"]} Contracts", text_alignment="center")
                            st.markdown(f"##### Result: :red[-{format_currency(abs(trade["profit_loss"]))}] ", text_alignment="center")
                            st.markdown(f"{trade["result"]}", text_alignment="center")
                            st.markdown(f"{trade["lesson"]}", text_alignment="center")
                    footer_container = st.container(border=True)
                    with footer_container:
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            st.caption(f"Difficulty: {trade["difficulty"]}", text_alignment="center")
                        with col2:
                            st.caption(f"Bank Balance: {format_currency(trade["ending_bank"])}", text_alignment="center")
                        with col3:
                                st.caption(f"Category: {trade["category"]}", text_alignment="center")

            else:
                with st.expander(f"Scenario {i+1}: {trade['ticker']} {trade["option_type"]} Option {trade['action']}: {format_currency(trade["profit_loss"])}"):
                    st.subheader(f"{trade["title"]} ({trade["date"]})", text_alignment="center")
                    st.markdown(f" ##### {trade["description"]}", text_alignment="center")
                    spec_col, result_col = st.columns([1, 2.5], border=True)
                    with spec_col:
                            st.markdown(f" ##### Option Specifications:", text_alignment="center")
                            st.markdown(f"###### Stock Price: {format_currency(trade["stock_price"])}", text_alignment="center")
                            st.markdown(f"###### Strike Price: {format_currency(trade["strike_price"])}", text_alignment="center")
                            st.markdown(f"###### Time Till Expiry (Months): {trade["time_till_expiry"]}", text_alignment="center")
                            st.markdown(f"###### Volatility: {format_percent(trade["volatility"])}", text_alignment="center")
                            st.markdown(f"###### Risk Free Rate: {format_percent(trade["risk_free_rate"])}", text_alignment="center")
                            st.markdown(f"###### Option Type: {trade["option_type"]}", text_alignment="center")
                    with result_col:
                            st.markdown(f"##### Market Option Price: {format_currency(trade["option_price"])}", text_alignment="center")
                            st.markdown(f"##### Your Decision: {trade["action"]} {trade["num_contracts"]} {trade["option_type"]} Contracts", text_alignment="center")
                            st.markdown(f"##### Result: :grey[{format_currency(trade["profit_loss"])}] ", text_alignment="center")
                            st.markdown(f"{trade["result"]}", text_alignment="center")
                            st.markdown(f"{trade["lesson"]}", text_alignment="center")
                    footer_container = st.container(border=True)
                    with footer_container:
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            st.caption(f"Difficulty: {trade["difficulty"]}", text_alignment="center")
                        with col2:
                            st.caption(f"Bank Balance: {format_currency(trade["ending_bank"])}", text_alignment="center")
                        with col3:
                            st.caption(f"Category: {trade["category"]}", text_alignment="center")

        button_container = st.container(horizontal_alignment="center")
        with button_container:
            again_col, resources_col = st.columns(2)
            with again_col:
                if st.button("Play Again!", type="primary", use_container_width=True):
                    st.session_state.quiz_indices = quiz_df.sample(5).index.tolist()
                    st.session_state.quiz_position = 0
                    scenario_index = st.session_state.quiz_indices[st.session_state.quiz_position]
                    current_scenario = quiz_df.loc[scenario_index]
                    st.session_state.bank_value = 10000
                    st.session_state.bs_price = None
                    st.session_state.mc_price = None
                    st.session_state.quiz_submitted = False
                    st.session_state.last_action = None # Tracks take or skip
                    st.session_state.chosen_contracts = 0
                    st.session_state.quiz_history = [{} for _ in range(5)]
                    st.rerun()

            with resources_col:
                if st.button("Go to Resources!", type="primary", use_container_width=True):
                    st.session_state.quiz_indices = quiz_df.sample(5).index.tolist()
                    st.session_state.quiz_position = 0
                    scenario_index = st.session_state.quiz_indices[st.session_state.quiz_position]
                    current_scenario = quiz_df.loc[scenario_index]
                    st.session_state.bank_value = 10000
                    st.session_state.bs_price = None
                    st.session_state.mc_price = None
                    st.session_state.quiz_submitted = False
                    st.session_state.last_action = None # Tracks take or skip
                    st.session_state.chosen_contracts = 0
                    st.session_state.quiz_history = [{} for _ in range(5)]
                    st.session_state.page = "Resources"
                    st.rerun()
    else:
        scenario_index = st.session_state.quiz_indices[st.session_state.quiz_position]
        current_scenario = quiz_df.loc[scenario_index]
        if st.session_state.quiz_submitted:
            display_summary_scene(current_scenario)
        else:
            display_quiz_scenario(current_scenario)
