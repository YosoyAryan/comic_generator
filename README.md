# 🎨✨ AI Comic Story Generator for Kids

Welcome to the **AI Comic Generator** — a magical web app that transforms *boring plain text* or *dull topics* into **fun, illustrated comic stories**! 🌈🦸‍♂️📚 Perfect for children, parents, educators, or anyone who wants to **bring stories to life** with a sprinkle of AI imagination.

---

## 🚀 What It Does

This AI-powered Django app takes:
- A **topic** (e.g., "Saving Trees", "My Superhero Dog", "Space Adventure")
- A **comic style** (Disney, Marvel, Anime, DC Comics, or even facts about the universe!)
- A **language** of your choice (supports 10+ languages)
![WhatsApp Image 2025-05-18 at 12 06 12 PM](https://github.com/user-attachments/assets/179443be-1059-4be7-a5ad-53daf0e43929)

And generates:
- 🧠 A 3-part **funny or creative story** using LLMs
- 🎨 AI-generated **illustrated comic pages** (in chosen style)
- 📄 A downloadable **PDF comic book** with both story and artwork!
[Uploading comic_41189.pdf…]()

---

## 🧠 How It Works

It uses a combination of powerful tools:
- **LangChain + Groq + LLaMA model** to generate funny, creative storylines
- **Hugging Face Inference API** to generate comic-style images from story text
- **EasyGoogleTranslate** for multilingual support
- **Pillow** and **ReportLab** to design comic layouts and generate a shareable PDF

---

## 📦 Features

- ✍️ Topic-based AI storytelling
- 🎭 Multiple comic art styles (Marvel, Anime, Disney, etc.)
- 🌐 Multilingual story support (English, Hindi, Spanish, French, etc.)
- 📷 Image generation for each story part
- 📘 Comic book-style PDF output
- 🎨 Kid-friendly UI with full-screen immersive experience

---

## 🛠️ Installation

1. **Clone the repo**

bash
git clone https://github.com/your-username/comic_generator.git
cd comic_generator
`

2. **Create and activate a virtual environment**

bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate


3. **Install dependencies**

bash
pip install -r requirements.txt


4. **Create a `.env` file**

env
GROQ_API_KEY=your_groq_key
HUGGINGFACE_API_KEY=your_huggingface_key


5. **Run the server**

bash
python manage.py runserver


Visit `http://127.0.0.1:8000/` to start generating stories!

---

## 📁 Project Structure

![Screenshot 2025-05-18 160329](https://github.com/user-attachments/assets/33e412dc-949e-4f38-9fd4-f1e781ba5ff9)

---

## 🧸 Use Cases

* 📖 **Kids Education**: Teach concepts through fun comics.
* 🎨 **Storytelling Practice**: Help children build narratives.
* 🤹‍♂️ **Entertainment**: Generate bedtime stories with pictures.
* 🌍 **Multilingual Learning**: Promote language learning through stories.

---

## 💡 Example

Enter Topic: `The Lost Moon Rocket`
Style: `Anime`
Language: `French`

📘 Output:

* A 3-part adventurous comic story in French
* Anime-style comic illustrations
* A downloadable PDF of your comic book!

* Here's a sneak peek of the AI Comic Generator in action! *
![WhatsApp Image 2025-05-18 at 12 07 32 PM (1)](https://github.com/user-attachments/assets/370ee04d-c565-492d-96b6-85c98baab6d5)
![WhatsApp Image 2025-05-18 at 12 07 32 PM (2)](https://github.com/user-attachments/assets/47bde9cb-a559-4698-a71a-604d1d3a6e97)
![WhatsApp Image 2025-05-18 at 12 07 32 PM](https://github.com/user-attachments/assets/756e5f60-b772-4be6-86c7-a9086c0a7241)
---


## 🛡️ License
MIT License.
---

## 🧙‍♀️ Created With Magic By

> 🧠 GPT + LangChain + Groq
> 🎨 HuggingFace Inference API
> 🌍 EasyGoogleTranslate
> 🛠️ Django, Pillow, ReportLab

Happy Storytelling! 🚀🖍️

