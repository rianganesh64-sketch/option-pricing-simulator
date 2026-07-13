import streamlit as st
from ui_components.navbar import display_nav_bar

def display_tutorial():
    display_nav_bar("Home", "Simulator", "Quiz", "Resources")
    st.space("medium")
    st.title("Start Learning!", text_alignment="center")
    st.markdown(
        "Understand the basics before testing models in the simulator", text_alignment="center"
    )
    st.space("small")
    tutorial_cards = [
    {
        "title": "Welcome to the Tutorial!",
        "body": "Welcome! This tutorial will teach you the basics of options, option pricing, and how to use the simulator. By the end, you should be ready to test different inputs, compare pricing models, and make decisions in the quiz section. You'll learn the concepts here, test them out in the simulator, and apply them to real-world scenarios in the quiz. Have fun!",
        "definitions": "• **Simulator** — The tool that lets you change inputs and visualize how the results change."
        + "\n\n"
        + "• **Quiz** — A section where you apply what you learned to realistic market scenarios.",
    },
    {
        "title": "What Is a Stock?",
        "body": "A stock represents partial ownership in a company. Its price changes over time based on news, earnings, interest rates, investor expectations, and market conditions. In this app, the stock price is the starting point for pricing an option.",
        "definitions": "• **Stock** — A share of ownership in a company."
        + "\n\n"
        + "• **Stock Price** — The current market price of one share."
        + "\n\n"
        + "• **Underlying Asset** — The asset that an option is based on.",
    },
    {
        "title": "What Is an Option?",
        "body": "An option is a contract based on an underlying asset, such as a stock. It gives someone the right to buy or sell the stock at a specific price by a specific date. Options are useful because they let traders make decisions based on where they think a stock might move.",
        "definitions": "• **Option** — A financial contract based on another asset."
        + "\n\n"
        + "• **Contract** — An agreement with specific rules."
        + "\n\n"
        + "• **Expiration Date** — The date when the option ends.",
    },
    {
        "title": "Calls and Puts",
        "body": "There are two main types of options: calls and puts. A call option usually becomes more valuable when the stock price rises. A put option usually becomes more valuable when the stock price falls. In the simulator and quiz, choosing call or put changes how the option is priced.",
        "definitions": "• **Call Option** — An option connected to buying a stock at a fixed price."
        + "\n\n"
        + "• **Put Option** — An option connected to selling a stock at a fixed price."
        + "\n\n"
        + "• **Option Type** — Whether the option is a call or a put.",
    },
    {
    "title": "Strike Price",
    "body": "The strike price is the fixed price written into the option contract. For a call option, the strike price is the price where the buyer can buy the stock. For a put option, it is the price where the buyer can sell the stock. The relationship between the stock price and strike price strongly affects the option's value.",
    "definitions": "• **Strike Price** — The fixed price written into the option contract."
    + "\n\n"
    + "• **Stock Price vs Strike Price** — The comparison that helps determine whether an option is in the money or out of the money."
    + "\n\n"
    + "• **Option Value** — The estimated worth of the option based on the model and market conditions.",
    },
    {
    "title": "In the Money vs Out of the Money",
    "body": "Once you know the stock price and strike price, you can tell whether an option is in the money or out of the money. For a call option, it is in the money when the stock price is above the strike price. It is out of the money when the stock price is below the strike price. This matters in the simulator and quiz because it helps you judge how risky or realistic an option trade is.",
    "definitions": "• **In the Money Call** — A call option where the stock price is above the strike price."
    + "\n\n"
    + "• **Out of the Money Call** — A call option where the stock price is below the strike price."
    + "\n\n"
    + "• **At the Money** — When the stock price and strike price are very close.",
    },
    {
        "title": "Time to Expiration",
        "body": "Options only last for a limited time. More time usually gives the stock more chance to move, which can make the option more valuable. In this app, users enter time in months, but the model converts it into years.",
        "definitions": "• **Time to Expiration** — How long the option has before it ends."
        + "\n\n"
        + "• **Time Value** — Value that comes from the possibility of future movement."
        + "\n\n"
        + "• **Expiration** — The end of the option contract.",
    },
    {
        "title": "Volatility",
        "body": "Volatility measures how much a stock price tends to move. Higher volatility usually raises option prices because there is a greater chance the stock moves enough to make the option valuable. In the quiz, high-volatility scenarios may create more risk and more opportunity.",
        "definitions": "• **Volatility** — A measure of how much a stock price moves."
        + "\n\n"
        + "• **High Volatility** — Larger price swings."
        + "\n\n"
        + "• **Low Volatility** — Smaller price swings.",
    },
    {
        "title": "Risk-Free Rate",
        "body": "The risk-free rate is a theoretical interest rate used in pricing models. It helps adjust the value of money over time. In real finance, government bond or Treasury rates are often used as a rough estimate.",
        "definitions": "• **Risk-Free Rate** — A theoretical safe interest rate used in models."
        + "\n\n"
        + "• **Interest Rate** — The cost or reward of borrowing or lending money."
        + "\n\n"
        + "• **Discounting** — Adjusting future money into today's value.",
    },
    {
        "title": "What Is Black-Scholes?",
        "body": "Black-Scholes is a formula-based model for estimating the price of European options. It uses the stock price, strike price, time to expiration, risk-free rate, volatility, and option type. Because it is formula-based, the same inputs should give the same result every time.",
        "definitions": "• **Black-Scholes Model** — A formula used to estimate European option prices."
        + "\n\n"
        + "• **European Option** — An option that can only be exercised at expiration."
        + "\n\n"
        + "• **Deterministic** — Giving the same result every time for the same inputs.",
    },
    {
        "title": "What Is Monte Carlo Simulation?",
        "body": "Monte Carlo simulation estimates an option price by creating many possible future stock paths. It then averages the results. Because it uses randomness, the answer may change slightly between runs, especially when the number of simulations is low.",
        "definitions": "• **Monte Carlo Simulation** — A method that uses repeated random trials to estimate a result."
        + "\n\n"
        + "• **Simulation** — A computer-generated possible outcome."
        + "\n\n"
        + "• **Runtime** — How long the calculation takes.",
    },
    {
        "title": "What Is GBM?",
        "body": "GBM stands for Geometric Brownian Motion. It is a model used to create possible future stock price paths. The GBM graph does not show one guaranteed future. It shows several possible futures that help explain how Monte Carlo simulation works.",
        "definitions": "• **GBM** — A model for simulating possible stock price movements."
        + "\n\n"
        + "• **Path** — One possible future movement of the stock."
        + "\n\n"
        + "• **Randomness** — Unpredictable variation in the model.",
    },
    {
        "title": "Comparing the Models",
        "body": "The simulator compares Black-Scholes and Monte Carlo prices. If the results are close, the models are giving similar estimates. If they are far apart, the Monte Carlo simulation may need more trials, or the inputs may be creating a more difficult pricing situation.",
        "definitions": "• **Absolute Error** — The dollar difference between two prices."
        + "\n\n"
        + "• **Percent Error** — The difference shown as a percentage."
        + "\n\n"
        + "• **Model Comparison** — Looking at how two methods agree or disagree.",
    },
    {
        "title": "Real-World Application",
        "body": "In the real world, traders, analysts, and students use option pricing models to estimate whether an option seems expensive, cheap, risky, or fair. These models do not perfectly predict the market, but they help people think more clearly about risk, time, volatility, and possible outcomes.",
        "definitions": "• **Fair Value** — A model's estimate of what an option may be worth."
        + "\n\n"
        + "• **Market Price** — The price people are actually trading at."
        + "\n\n"
        + "• **Risk** — The chance that the result is different from what was expected.",
    },
    {
    "title": "Preparing for the Quiz",
    "body": "In the quiz, you will see realistic market scenarios based on real events. Your job is to read the scenario, use the simulator, and decide whether to take the trade or skip it. If you take the trade, you will choose how much of your bank to risk. The goal is not just to be right, but to make smart decisions with risk in mind.",
    "definitions": "• **Scenario** — A realistic situation based on market conditions."
    + "\n\n"
    + "• **Bank** — The amount of money you have available in the quiz."
    + "\n\n"
    + "• **Position Size** — How much money you choose to risk on one trade.",
    },
    {
        "title": "Important Limitation",
        "body": "This app is for learning, not financial advice. Real option prices can differ from model prices because of supply and demand, bid-ask spreads, dividends, early exercise, news events, and changing volatility. The simulator helps you understand the models, not predict the future perfectly.",
        "definitions": "• **Model** — A simplified version of the real world."
        + "\n\n"
        + "• **Assumption** — Something a model treats as true to make calculation possible."
        + "\n\n"
        + "• **Educational Tool** — A tool designed to help users learn.",
    },
]

    if "card_index" not in st.session_state:
        st.session_state.card_index = 0
    
    def display_card(card):
        card_container = st.container(border=True)
        with card_container:
            col1, col2, col3 = st.columns([1, 6.5, 1])
            with col2:
                st.markdown(f"###### Card {st.session_state.card_index + 1} of {len(tutorial_cards)}", text_alignment="center")
                st.title(card["title"], text_alignment="center")
                st.markdown("##### " + card["body"], text_alignment="center")
                st.space("xxsmall")
                st.markdown("#### **Important Definitions:**", text_alignment="center")
                st.info(
                card["definitions"])

    current_card = tutorial_cards[st.session_state.card_index]

    is_last_card = st.session_state.card_index == len(tutorial_cards) - 1

    card_col1, card_col, card_col3 = st.columns([1, 2.5, 1])
    with card_col:
        display_card(current_card)
        if not is_last_card:
            if st.session_state.card_index == 0:
                left_col, button_col, right_col = st.columns([1, 2.5, 1])
                with button_col:
                    with st.container(horizontal_alignment="center"):
                        if st.button("Let's go!", use_container_width=True):
                            st.session_state.card_index += 1
                            st.rerun()
            else:
                left_button_col, right_button_col = st.columns(2)
                with left_button_col:
                    with st.container(horizontal_alignment="center"):
                        if st.button("⟵ Previous", use_container_width=True):
                            st.session_state.card_index -= 1
                            st.rerun()
                with right_button_col:
                    with st.container(horizontal_alignment="center"):
                        if st.button("Next ⟶", use_container_width=True):
                            st.session_state.card_index += 1
                            st.rerun()
        else:
            restart_col, exit_col = st.columns(2)
            with restart_col:
                with st.container(horizontal_alignment="center"):
                    if st.button("Restart Tutorial", use_container_width=True):
                        st.session_state.card_index = 0
                        st.rerun()
            with exit_col:
                with st.container(horizontal_alignment="center"):
                    if st.button("Done!: Go to simulator", use_container_width=True):
                        st.session_state.card_index = 0
                        st.session_state.page = "Simulator"
                        st.rerun()
