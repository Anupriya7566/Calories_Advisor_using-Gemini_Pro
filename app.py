# Import the necessary libraries and modules
from dotenv import load_dotenv
import streamlit as st
import streamlit_authenticator as stauth
import os
import google.generativeai as genai
from PIL import Image

# Configure the Google Gemini Pro Vision API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Define the function to get the Gemini response
def get_gemini_response(input_prompt, image):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input_prompt, image[0]])
    return response.text

# Define the function to set up the image data
def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Initialize the Streamlit app
st.set_page_config(page_title="Calories Advisor APP")

# Display the header
st.header("Calories Advisor APP")

# Create an input field for the prompt
input = st.text_input("Input Prompt:", key="input")

# Create a file uploader for the image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# Display the uploaded image, if available
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

# Create the submit button
submit = st.button("Tell me the total calories")

# Define the input prompt
input_prompt = """
You are an expert in nutritionist where you need to see the food items from the image
and calculate the total calories, also provide the details of every food items with calories intake
in the below format:

1. Item 1 - no of calories
2. Item 2 - no of calories
----
----

Give me advice on whether it is good or not for health.
"""

# If the submit button is clicked
if submit:
    # Set up the image data
    image_data = input_image_setup(uploaded_file)
    
    # Get the response from the Gemini Pro Vision API
    response = get_gemini_response(input_prompt, image_data)
    
    # Display the response
    st.subheader("The Response is")
    st.write(response)
