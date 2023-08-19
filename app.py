import os

import replicate
import streamlit as st
from streamlit_chat import message
from elevenlabs import generate
from langchain import PromptTemplate
from langchain.chains import LLMChain
import openai

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_response(text):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [
            {
                "role": "user",
                "content" : text            }
        ]
    )
    return response['choices'][0]['message']['content']

def get_text():
    input_text = st.text_input("Chat with me", key="input_text")
    return input_text

# Store and track user input and generated text in session state
if 'past' not in st.session_state:
    st.session_state['past'] = [] # User input text

# Store and track AI generated text in session state
if 'generated' not in st.session_state:
    st.session_state['generated'] = [] # AI generated text


def main():
    st.title("Personal Chatbot")

    user_input = get_text()

    if user_input:
        response = generate_response(user_input)
        st.session_state['past'].append(user_input)
        st.session_state['generated'].append(response)
    

    # Display all generated text and user input
    if st.session_state['generated']:
        for i in range(len(st.session_state['generated'])):
            message(st.session_state['past'][i], is_user=True)
            message(st.session_state['generated'][i])
            
    

if __name__ == "__main__":
    main()

