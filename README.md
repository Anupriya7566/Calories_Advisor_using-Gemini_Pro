# Health Management APP

## Introduction

This code sets up a Streamlit web application for a "Calories Advisor APP." The purpose of the app is to allow users to input a prompt and upload an image of food items. The app then utilizes Google Gemini Pro Vision API to analyze the image, identify food items, calculate the total calories, and provide advice on whether the food is good for health or not. The user interface includes input fields for the prompt and image upload, as well as a button to trigger the analysis. Once the analysis is complete, the app displays the response, which includes details of the food items detected, their respective calorie counts, and advice on their healthiness.

## Key Concepts

### Streamlit :
Streamlit is an open-source Python library that allows you to create web applications for machine learning and data science projects. It provides a simple and intuitive way to build interactive and customizable user interfaces.

### Google Gemini Pro Vision API :
The Google Gemini Pro Vision API is a powerful tool for image analysis and recognition. It can identify objects, faces, and text in images, as well as provide information about their attributes and characteristics.

### PIL (Python Imaging Library) :
PIL is a library in Python that adds support for opening, manipulating, and saving many different image file formats. It provides a wide range of image processing capabilities, including resizing, cropping, and enhancing images.

## Code Structure

The code is structured as follows:

1. Import the necessary libraries and modules:
   - `dotenv`: A library for loading environment variables from a .env file.
   - `streamlit`: The Streamlit library for creating web applications.
   - `streamlit_authenticator`: A library for authenticating users in Streamlit apps.
   - `os`: The OS module for interacting with the operating system.
   - `google.generativeai`: The Google Gemini Pro Vision API module for image analysis.
   - `PIL`: The Python Imaging Library for image processing.

2. Configure the Google Gemini Pro Vision API by loading the API key from the environment variables.

3. Define a function `get_gemini_response` that takes an input prompt and an image as parameters. This function uses the Google Gemini Pro Vision API to generate a response based on the input prompt and the image.

4. Define a function `input_image_setup` that takes an uploaded file as a parameter. This function checks if a file has been uploaded, reads the file into bytes, and returns the image parts.

5. Initialize the Streamlit app and set the page configuration.

6. Create the user interface:
   - Display the header "Calories Advisor APP".
   - Create an input field for the prompt.
   - Create a file uploader for the image.
   - Display the uploaded image, if available.
   - Create a submit button "Tell me the total calories".

7. Define an input prompt that explains the expected format of the prompt and the desired output.

8. If the submit button is clicked, call the `input_image_setup` function to set up the image data.

9. Call the `get_gemini_response` function to get the response from the Google Gemini Pro Vision API.

10. Display the response in a subheader and write it to the Streamlit app.

## Conclusion

This code sets up a Streamlit web application for a "Calories Advisor APP" using the Google Gemini Pro Vision API to analyze images of food items and provide advice on their healthiness. It allows users to input a prompt and upload an image, displaying the API response. This code provides a foundation for building nutrition or health-related applications based on food image analysis.
