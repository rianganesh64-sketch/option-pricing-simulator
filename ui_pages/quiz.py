import streamlit as st
import pandas as pd
from pathlib import Path
from src.utils import format_currency
from ui_components.navbar import display_nav_bar

CSV_PATH = Path("data/real_world_option_quiz_scenarios.csv")

@st.cache_data
def load_quiz_data():
    return pd.read_csv(CSV_PATH)

def display_quiz():
    display_nav_bar("Home", "Tutorial", "Simulator", "Resources")
    st.space("medium")
    st.title("Quiz", text_alignment="center")
    st.markdown("Test your knowledge with real world scenarios!", text_alignment="center")

    quiz_df = load_quiz_data()
    
    if "quiz_indices" not in st.session_state:
        st.session_state.quiz_indices = quiz_df.sample(5).index.tolist()
    
    if "quiz_position" not in st.session_state:
        st.session_state.quiz_position = 0

    if "bank" not in st.session_state:
        st.session_state.bank = 10000

    if "quiz_answered" not in st.session_state:
        st.session_state.quiz_answered = False

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