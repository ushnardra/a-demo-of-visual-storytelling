import base64
import os
import mimetypes
from google import genai
from google.genai import types

def save_binary_file(file_name, data):
    with open(file_name, "wb") as f:
        f.write(data)

def generate():
    
    client = genai.Client(api_key="AIzaSyCaYfT-2Ut9eTckGgBEPnLBKVGgBXErQ-g")

    Preamble = """You are an advanced AI image generator , you will never generate any texts , you are built for only images. 
    Generate high-quality, HD, realistic human images with exceptional detail and clarity. 
    The image should be in a landscape format (16:9 aspect ratio) with vibrant colors and sharp resolution.
    Ensure realistic lighting, accurate textures, and a professional finish.
    """

    user_prompt = input("Enter the text prompt for image generation: ") 
    full_prompt = Preamble + "\n\n" + user_prompt
    contents = [full_prompt] 


    model = "gemini-2.0-flash-exp-image-generation"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=user_prompt),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        response_modalities=["image", "text"],
        safety_settings=[
            types.SafetySetting(
                category="HARM_CATEGORY_CIVIC_INTEGRITY",
                threshold="OFF",  # Off
            ),
        ],
        response_mime_type="text/plain",
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        if not chunk.candidates or not chunk.candidates[0].content or not chunk.candidates[0].content.parts:
            continue
        if chunk.candidates[0].content.parts[0].inline_data:
            file_name = "generated_output"
            inline_data = chunk.candidates[0].content.parts[0].inline_data
            file_extension = mimetypes.guess_extension(inline_data.mime_type)
            save_binary_file(f"{file_name}{file_extension}", inline_data.data)
            print(f"File saved: {file_name}{file_extension}")
        else:
            print(chunk.text)

if __name__ == "__main__":
    generate()
