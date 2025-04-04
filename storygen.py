from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import subprocess
import PIL.Image

subprocess.run(["C:\PROJECTS\Story\.venv\Scripts\python.exe", "charactercreator.py"], check=True)
# Open the generated image file

image = PIL.Image.open('C:\PROJECTS\INTEL UNNATI\generated_output.png')

client = genai.Client(api_key="AIzaSyCaYfT-2Ut9eTckGgBEPnLBKVGgBXErQ-g")

preamble=""" generate 10 slides with story script and images.
The story should have a beginning and an end.
same character consistency and high-quality images.
images should show the same charcter in different scenes and situations.
images should  in vibrant colors and sharp resolution.
Ensure realistic lighting, accurate textures, and a professional finish.
"""
user_prompt = input("Enter the story: ")
full_prompt = preamble + "\n\n" + user_prompt
text_input = types.Content(
    role="user",
    parts=[
        types.Part.from_text(text=full_prompt),
    ],
)

response = client.models.generate_content(
    model="gemini-2.0-flash-exp-image-generation",
    contents=[text_input, image],
    config=types.GenerateContentConfig(
      response_modalities=['Text', 'Image']
    )
)

image_counter = 0
for part in response.candidates[0].content.parts:
  if part.text is not None:
    print(part.text)
  elif part.inline_data is not None:
    image = Image.open(BytesIO(part.inline_data.data))
    image.save(f"generated_image_{image_counter}.png")
    image_counter += 1
    image.show()