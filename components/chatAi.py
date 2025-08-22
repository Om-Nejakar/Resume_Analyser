import streamlit as st
from dotenv import load_dotenv
import os

# OpenAI
from openai import OpenAI

# Gemini
from google import genai
from google.genai import types


def chatAi_ui(model_choice, start_chat):
    load_dotenv()
    api_key = os.environ['GEMINI_API_KEY']
    st.info("AI Chat mode opened!")

    if start_chat and model_choice and model_choice != "-- Select a model --":
        st.success(f"Chat started with {model_choice}")

        # Initialize conversation
        if "messages" not in st.session_state:
            st.session_state.messages = [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "assistant", "content": "Hello! How can I help you today?"},
            ]

        # Display conversation
        for msg in st.session_state.messages:
            if msg["role"] == "user":
                st.markdown(f"**You:** :orange[{msg['content']}]")
            elif msg["role"] == "assistant":
                st.text_area("AI:", msg['content'], height=150)

        # User input
        user_prompt = st.text_input(
            "Enter your question or instruction for the resume", 
            value="",
            key="input_area"
        )

        if st.button("Ask AI") and user_prompt:
            st.session_state.messages.append({"role": "user", "content": user_prompt})

            with st.spinner("Thinking..."):

                # --- OpenAI ---
                if model_choice.startswith("openai"):
                    client = OpenAI(
                        base_url="https://openrouter.ai/api/v1",
                        api_key=os.environ.get("OPENROUTER_API_KEY"),
                    )
                    response = client.chat.completions.create(
                        model=model_choice,
                        messages=st.session_state.messages
                    )
                    content = response.choices[0].message.content

                # --- Gemini ---
                elif model_choice.startswith("gemini"):
                    client = genai.Client(api_key=api_key)

                    response = client.models.generate_content(
                        model=model_choice,  # e.g. "gemini-2.5-flash"
                        contents=user_prompt,
                        config=types.GenerateContentConfig(
                            thinking_config=types.ThinkingConfig(thinking_budget=0)  # disables thinking
                        ),
                    )
                    content = response.text

                else:
                    content = "Unknown model choice."

            # Save and display response
            st.session_state.messages.append({"role": "assistant", "content": content})
            st.rerun()
