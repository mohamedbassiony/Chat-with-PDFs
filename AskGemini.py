from dotenv import load_dotenv

# Loading all the environment variables
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

# Make configuration to the API Key
genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))


# Function to load Gemini pro model and get responses
model = genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response=model.generate_content(question)
    return response.text
                
# Initialize our streamlit app

st.set_page_config(page_title="Q&A Demo")

st.header("Gemini LLM Application, Ask anything:")

input = st.text_input("Ask the Question: ", key = "input")
submit = st.button("Submit")

# When submit is cliked
if submit:
    response = get_gemini_response(input)
    st.subheader("The Response is:")
    st.write(response)