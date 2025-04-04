# VISUAL STORYTELLING AI
​A web app that creates realistic character images and visual narratives. Users input a description or story idea to receive engaging storytelling content with consistent character imagery. Ideal for creative projects, educational tools, and interactive storytelling.
# 📖 Advanced Visual Storytelling with AI

This project generates a 10-slide visual story using **Google Gemini AI**, integrating **character generation, AI-driven storytelling, and image generation**. Each story scene includes AI-generated text and images.

## 🚀 Features
- **Character Generation**: Uses AI to create unique characters.
- **Story Generation**: Produces a script-based story format.
- **AI Image Generation**: Creates and modifies images based on the story.
- **Automated Pipeline**: Runs seamlessly in sequence.

## 🛠️ Setup Instructions

### 1️⃣ Install Dependencies
Ensure you have Python installed, then install the required libraries:
```sh
pip install google-generativeai pillow
```

### 2️⃣ Set Up API Key
Obtain a **Google Gemini API Key** and set it as an environment variable:
```sh
export GEMINI_API_KEY="your-api-key-here"
```

### 3️⃣ Run the Storytelling Pipeline
Execute the main script to generate a full AI-powered visual story:
```sh
python main.py
```

## 📂 Project Structure
```
📂 AI-Visual-Storytelling
│-- 📄 main.py                  # Main script for full storytelling pipeline
│-- 📄 gemini_user_prompt.py     # Character generation script
│-- 📄 image_prompts.txt         # Story scene descriptions for image generation
│-- 📄 gemini-native-image.png   # Initial AI-generated image
│-- 📄 updated_image_*.png       # AI-modified story images
│-- 📄 README.md                 # Project documentation
```

## 📝 How It Works
1. **Character Generation**: Runs `gemini_user_prompt.py` to create characters.
2. **Story Processing**: Reads `image_prompts.txt` to generate scene descriptions.
3. **Image Generation**: AI processes `gemini-native-image.png` and modifies it per scene.

## 📌 Notes
- The script automatically saves images as `updated_image_1.png`, `updated_image_2.png`, etc.
- Modify `image_prompts.txt` to customize the story themes.
- Adjust AI settings in `main.py` for better results.

## 🎬 Example Output
A sample 10-slide AI-generated visual story:
1️⃣ **Slide 1**: "A knight stands at the castle gates..." 🖼️ Image
2️⃣ **Slide 2**: "The journey begins through the dark forest..." 🖼️ Image
...
🔟 **Slide 10**: "The hero faces the final battle!" 🖼️ Image

## 🤖 Future Enhancements
- 🎭 More dynamic storytelling options.
- 🌍 Multi-language support.
- 🎨 Enhanced AI-generated visuals.

## 🎉 Contribute & Support
Feel free to **fork, modify, and enhance** this project! Star ⭐ it if you find it useful. Contributions are welcome!

---
Developed by Ushnardra Ghosh

