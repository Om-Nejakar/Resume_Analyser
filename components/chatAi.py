import streamlit as st
from dotenv import load_dotenv
import os
from components.mongodb import MongoDBChat

# OpenAI
from openai import OpenAI

# Gemini
import google.generativeai as genai
from google.generativeai import types

mongo = MongoDBChat()

def chatAi_ui(model_choice, start_chat):
    load_dotenv()
    api_key = os.environ['GEMINI_API_KEY']
    

    st.info("AI Chat mode opened!")
    session_id = "user123"

    if start_chat and model_choice and model_choice != "-- Select a model --":
        st.success(f"Chat started with {model_choice}")

        # Initialize conversation
        if "messages" not in st.session_state:
            st.session_state.messages = mongo.load_chat(session_id) or []

        # Display conversation
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.write(msg["content"])

        # User input
        user_prompt = st.chat_input("Type your message")

        if user_prompt:
            st.session_state.messages.append({"role": "user", "content": user_prompt})
            mongo.save_chat(session_id, st.session_state.messages)

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
                    genai.configure(api_key=api_key)

                    model = genai.GenerativeModel(model_choice)  # e.g. "gemini-1.5-flash"
                    response = model.generate_content(
                        user_prompt,
                        generation_config=types.GenerationConfig(
                            # add extra options here if you want
                        ),
                    )
                    content = response.text

                else:
                    content = "Unknown model choice."

            # Save and display response
            st.session_state.messages.append({"role": "assistant", "content": content})
            mongo.save_chat(session_id, st.session_state.messages)
            st.rerun()
