import streamlit as st
import openai
import requests
from dotenv import load_dotenv
import os

load_dotenv()
st.title("Text To Image Generator (DALL·E)")
# api_key=st.sidebar.text_input("Enter OpenAI API Key")
openai.api_key = os.getenv("OPENAI_API_KEY")
prompt = st.text_input("Enter your description")
if prompt:
    with st.spinner("Generating..."):
     response = openai.images.generate(
                model = "dall-e-3",
                prompt=prompt,
                quality = "standard",
                size="1024x1024"
     )
     Image_url = response.data[0].url
    
    # download the image content
     img_data = requests.get(Image_url).content
      # Layout: image + download
     col1, col2 = st.columns([4, 1])
     with col1:
      st.image(Image_url, caption="Generated Image", use_container_width=True)
     with col2:
        # add download button
        st.download_button(
            label="⬇️download image",
            data = img_data,
            file_name="image_from_prompt.png",
            mime="image/png"
        )
