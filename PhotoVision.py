from dotenv import load_dotenv

# Loading all the environment variables
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

# Make configuration to the API Key
genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))


# Function to load Gemini pro model and get responses
model = genai.GenerativeModel("gemini-pro-vision")
def get_gemini_response(input, image):
    if input != "":
        response=model.generate_content([input,image])
    else:
        response=model.generate_content(image)
    return response.text

# Initialize our streamlit app
st.set_page_config(page_title="Gemini Image Demo")

st.header("Description Photo Application")
input = st.text_input("Do you have spacific request about the photo: ", key = "input")

uploaded_file = st.file_uploader("Choose an image...", type = ["jpg", "jpeg", "png"])
submit = st.button("Tell me about the image")
image=""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)


# If submit is clicked
if submit:

    response = get_gemini_response(input, image)
    st.subheader("The Response is:")
    st.write(response)