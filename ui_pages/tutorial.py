import streamlit as st

def display_tutorial():
    col1, col2, col3, col4 = st.columns(4, border=False)
    with col1:
        if st.button("Home", use_container_width=True, type="tertiary"):
            st.session_state.page = "Home"
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
    st.title("Tutorial", text_alignment="center")
    tutorial_cards = [
        {
            "title": "Card one",
            "body": "This is card one",
            "definitions": "Defintions of card one",
        },
        {
            "title": "card two",
            "body": "This is card two",
            "definitions": "definitions of card two",
        },
    ]

    if "card_index" not in st.session_state:
        st.session_state.card_index = 0
    
    def display_card(card):
        st.markdown("## " + card["title"])
        st.write(card["body"])
        st.info(card["definitions"])

    current_card = tutorial_cards[st.session_state.card_index]

    display_card(current_card)

    is_last_card = st.session_state.card_index == len(tutorial_cards) - 1
    if not is_last_card:
        if st.button("Next Card"):
            st.session_state.card_index += 1
            st.rerun()
    else:
        restart_col, exit_col = st.columns(2)

        with restart_col:
            if st.button("Restart Tutorial", use_container_width=True):
                st.session_state.card_index = 0
                st.rerun()

        with exit_col:
            if st.button("Go to simulator", use_container_width=True):
                st.session_state.card_index = 0
                st.session_state.page = "Simulator"
                st.rerun()



