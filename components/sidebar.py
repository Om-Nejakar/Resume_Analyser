import streamlit as st

def sidebar_ui():
    st.header(":rainbow[YouVa-Chat]", divider=True)

    if "mode" not in st.session_state:
        st.session_state.mode = False
    if "chat_ai_open" not in st.session_state:
        st.session_state.chat_ai_open = False

    if "model_choice" not in st.session_state:
        st.session_state.model_choice = "-- Select a model --"
    if "chat_started" not in st.session_state:
        st.session_state.chat_started = False

    if st.button("Home"):
        st.session_state.mode = "home"

    if st.button("Chat with Ai"):
        st.session_state.mode = "chat"

    if st.button("Analyse Resume"):
        st.session_state.mode = "resume"

    if st.session_state.mode == "chat":
        if st.session_state.mode == "chat":
            st.session_state.model_choice = st.selectbox(
                "Choose the Model to interact with",
                ("-- Select a model --", "gemini-2.5-flash"),
                index=("-- Select a model --", "gemini-2.5-flash").index(st.session_state.model_choice)
            )
        if st.button("Start Chat"):
            st.session_state.chat_started = True

    return st.session_state.model_choice, st.session_state.chat_started, st.session_state.mode