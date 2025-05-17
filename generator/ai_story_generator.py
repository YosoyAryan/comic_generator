# dashboard/ai_story_generator.py

import os
import io
import random
from PIL import Image, ImageDraw, ImageFont, ImageOps
from reportlab.pdfgen import canvas
from easygoogletranslate import EasyGoogleTranslate
from langchain_groq import ChatGroq
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

# Load keys securely
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
HF_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

# Language mapping
LANGUAGES = {
    "English": "en", "Spanish": "es", "French": "fr", "Hindi": "hi",
    "Arabic": "ar", "Bengali": "bn", "Telugu": "te", "Marathi": "mr",
    "Tamil": "ta", "Urdu": "ur", "Gujarati": "gu", "Kannada": "kn",
    "Odia": "or", "Punjabi": "pa"
}

class TranslateHelper:
    def __init__(self):
        self.translator = EasyGoogleTranslate()

    def lang_translate(self, text, target_lang):
        return text if target_lang == "en" else self.translator.translate(text, target_lang)

def wrap_text(text, font, max_width):
    lines, line = [], []
    for word in text.split():
        test_line = ' '.join(line + [word])
        if font.getlength(test_line) > max_width and line:
            lines.append(' '.join(line))
            line = [word]
        else:
            line.append(word)
    if line:
        lines.append(' '.join(line))
    return lines

def rounded_corners(image, radius):
    mask = Image.new("L", image.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle([(0, 0), image.size], radius, fill=255)
    result = ImageOps.fit(image, mask.size, centering=(0.5, 0.5))
    result.putalpha(mask)
    return result

def ai_story_generator(topic, style, target_language):
    llm = ChatGroq(
        temperature=0.6,
        groq_api_key=GROQ_API_KEY,
        model="gemma-7b-it"
    )
    translator = TranslateHelper()

    styles = {
        "Disney Princes": "funny disney with cinderella, snow white or mickey mouse style",
        "Marvel": "funny marvel with avengers, captain america, hulk, thor, iron man or spiderman style",
        "Anime": "funny anime with naruto, zoro, death note, demon slayer, one punch man or dragon ball z style",
        "DC Comics": "funny batman style",
        "Observable Universe": "interesting story about facts of universe"
    }

    style_prompt = styles.get(style, "funny story")
    noise = random.randint(1000, 999999)
    story_prompt = (
        f"In 3 phrases, noise {noise}, separate each part with blank lines. "
        f"Narrate a {style_prompt} about '{topic}'. Each phrase ~100 words."
    )

    try:
        story = llm.invoke(story_prompt).content.strip()
        phrases = story.split("\n\n")
    except Exception as e:
        return None, f"LLM error: {e}"

    output_dir = os.path.join("media", f"comic_{random.randint(1, 99999)}")
    os.makedirs(output_dir, exist_ok=True)

    # Background and font
    bg_path = "static/dashboard/comic_bg.jpg"
    font_path = "static/dashboard/NotoSans.ttf"
    if not os.path.exists(font_path):
        font_path = "arial.ttf"

    background = Image.open(bg_path)
    bg_w, bg_h = background.size
    gap = 20
    text_h = bg_h // 4
    img_h = bg_h - text_h - 3 * gap

    image_paths = []
    pdf_path = os.path.join(output_dir, "comic_story.pdf")
    c = canvas.Canvas(pdf_path, pagesize=(bg_w, bg_h))

    client = InferenceClient(token=HF_API_KEY)

    for i, phrase in enumerate(phrases):
        translated = translator.lang_translate(phrase, LANGUAGES.get(target_language, "en"))
        try:
            img = client.text_to_image(f"{translated}, style {style}, noise {noise}", model="Shibaking/comic_style")

            img = rounded_corners(img.resize((bg_w - 2 * gap, img_h)), radius=20)
            img = ImageOps.expand(img, border=5, fill="black")

            white_box = Image.new("RGBA", (bg_w - 2 * gap, text_h), "orange")
            draw = ImageDraw.Draw(white_box)

            font_size = 120
            font = ImageFont.truetype(font_path, size=font_size)
            wrapped = wrap_text(translated, font, white_box.width - 40)

            while True:
                text_height = sum(font.getbbox(line)[3] - font.getbbox(line)[1] for line in wrapped) + 5 * len(wrapped)
                if text_height <= text_h or font_size <= 10:
                    break
                font_size -= 2
                font = ImageFont.truetype(font_path, size=font_size)
                wrapped = wrap_text(translated, font, white_box.width - 40)

            y = (text_h - text_height) // 2
            for line in wrapped:
                w = font.getlength(line)
                draw.text(((white_box.width - w) / 2, y), line, font=font, fill="black")
                y += font.getbbox(line)[3] - font.getbbox(line)[1] + 5

            full_image = Image.new("RGBA", (bg_w, bg_h), (255, 255, 255, 0))
            full_image.paste(background, (0, 0))
            full_image.paste(white_box, (gap, gap), white_box)
            full_image.paste(img, (gap, text_h + 2 * gap), img)

            image_path = os.path.join(output_dir, f"page_{i + 1}.png")
            full_image.convert("RGB").save(image_path)
            c.drawImage(image_path, 0, 0, width=bg_w, height=bg_h, mask='auto')
            c.showPage()
            image_paths.append(image_path)
        except Exception as e:
            print(f"Error with phrase {i+1}: {e}")

    c.save()
    return image_paths, pdf_path
