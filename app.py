import streamlit as st
import subprocess
import os
import time
from PIL import Image
from io import BytesIO
from google import genai
from google.genai import types

# ------------------------
# Configuration & File Paths
# ------------------------
# Update these paths to match your environment
CHARACTER_IMAGE_PATH = "C:/PROJECTS/INTEL UNNATI/generated_output.png"
CHARACTER_SCRIPT_PATH = "charactercreator.py"
PYTHON_ENV_PATH = "C:/PROJECTS/Story/.venv/Scripts/python.exe"

# Initialize the Google API Client with your API key
genai_client = genai.Client(api_key="AIzaSyCaYfT-2Ut9eTckGgBEPnLBKVGgBXErQ-g")

# ------------------------
# Streamlit App Layout
# ------------------------
st.set_page_config(page_title="AI Character & Story Generator", layout="wide")
st.title("AI Character & Story Generator")
menu = st.sidebar.radio("Navigation", ["Character Generation", "Story Generation"])

# ------------------------
# Character Generation Section
# ------------------------
if menu == "Character Generation":
    st.header("🎭 Generate a Character")
    character_prompt = st.text_input("Enter character description:")

    if st.button("Generate Character"):
        with st.spinner("Generating character..."):
            try:
                # Run the character generator script using the specified Python environment
                process = subprocess.run(
                    [PYTHON_ENV_PATH, CHARACTER_SCRIPT_PATH],
                    check=True, capture_output=True, text=True
                )
                st.text("Process Output:\n" + process.stdout)
                st.text("Process Error:\n" + process.stderr)

                # Wait up to 10 seconds for the image to be created
                timeout = 10
                start_time = time.time()
                while not os.path.exists(CHARACTER_IMAGE_PATH):
                    if time.time() - start_time > timeout:
                        st.error("Character generation took too long. Please try again.")
                        break
                    time.sleep(1)

                # If the image exists, display it in the app
                if os.path.exists(CHARACTER_IMAGE_PATH):
                    st.image(CHARACTER_IMAGE_PATH, caption="Generated Character", use_container_width=True)
                else:
                    st.error("Image not found! Please check the character generator script.")
            except subprocess.CalledProcessError as e:
                st.error(f"Error running character generator:\n{e.stderr}")

# ------------------------
# Story Generation Section
# ------------------------
elif menu == "Story Generation":
    st.header("📖 Generate a Story")
    story_prompt = st.text_area("Enter your story idea:")

    if st.button("Generate Story"):
        if not os.path.exists(CHARACTER_IMAGE_PATH):
            st.error("Please generate a character first!")
        else:
            with st.spinner("Generating story and images..."):
                try:
                    # Open the character image and prepare it as bytes
                    image = Image.open(CHARACTER_IMAGE_PATH)
                    buffer = BytesIO()
                    image.save(buffer, format="PNG")
                    buffer.seek(0)

                    # Build a prompt by combining a preamble with the user's story idea.
                    preamble = (
                        "Generate 10 slides with a story script and images. "
                        "The story should have a clear beginning and end and maintain the same character across all slides. "
                        "Images should be high-quality, realistic, and vibrant."
                    )
                    full_prompt = f"{preamble}\n\n{story_prompt}"

                    # Create the content object for the API
                    text_input = types.Content(
                        role="user",
                        parts=[types.Part.from_text(text=full_prompt)]
                    )

                    # Call the model to generate content (both text and image)
                    response = genai_client.models.generate_content(
                        model="gemini-2.0-flash-exp-image-generation",
                        contents=[text_input, types.Part.from_data(data=buffer.read(), mime_type="image/png")],
                        config=types.GenerateContentConfig(response_modalities=['Text', 'Image'])
                    )

                    # Process the response: accumulate text and save any generated images
                    output_text = ""
                    image_paths = []
                    for i, part in enumerate(response.candidates[0].content.parts):
                        if part.text:
                            output_text += part.text + "\n"
                        elif part.inline_data:
                            img = Image.open(BytesIO(part.inline_data.data))
                            img_path = f"generated_image_{i}.png"
                            img.save(img_path)
                            image_paths.append(img_path)

                    st.subheader("Generated Story Text")
                    st.write(output_text)

                    st.subheader("Generated Story Images")
                    for img_path in image_paths:
                        st.image(img_path, use_container_width=True)

                except Exception as e:
                    st.error(f"Error generating story: {str(e)}")
