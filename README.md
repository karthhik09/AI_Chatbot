# 🤖 Doraemon - Interactive Python Tutor

## 🎯 Overview

**Doremon** is a voice-interactive Python tutor powered by Google Gemini AI. It listens to your questions through your microphone, processes them using the Gemini AI model, and responds with concise Python-related answers. Designed to be interactive and beginner-friendly, Doremon helps users learn Python through voice-based conversations.

---

## ✨ Features

- 🎙️ **Speech Recognition (STT):** Understands your spoken input using `SpeechRecognition`.
- 🔊 **Text-to-Speech (TTS)**: Responds verbally using `pyttsx3`, simulating a conversational tutor.
- 🤖 **AI-Powered Responses**: Uses Google Generative AI (`gemini-pro` model) for intelligent and concise responses.
- 🧠 **Interactive Learning**: Reacts to commands like "explain in detail" for deeper explanations.
- 🚪 **Exit Command**: Say "exit" anytime to stop the session.

---

## 🛠️ Installation

### ✅ Prerequisites

Make sure you have the following installed:

- Python 3.8 or higher

### 📦 Required Python Libraries

- `google-generativeai`
- `SpeechRecognition`
- `pyttsx3`

---

## 🔐 Setup

1. **Clone the Repository**
   - Run the following commands in your terminal:
     
     ```bash
     git clone <your-repo>   # Replace <your-repo> with GitHub repository link
     cd <your-repo-folder>   # Replace <your-repo-folder> with your project folder name
     ```
     
2. **Create a Virtual Environment**
   - It's recommended to use a virtual environment to manage dependencies.
   - Run the following line in your terminal which will create a virtual environment named `myenv`:
     
     ```bash
     python3 -m venv myenv
     ```
     
3. **Activate the Virtual Environment**
   - On macOS/Linux:
     
     ```bash
     source myenv/bin/activate
     ```
     
   - On Windows:
     
     ```bash
     myenv\Scripts\activate
     ```
    
4. **Install Dependencies**
   - If you'd prefer to install all required packages at once, you can use the provided `requirements.txt` file:
     
     ```bash
     pip3 install -r requirements.txt
     ```
     
   **(Alternative Method for step 4)**:
   - Once the virtual environment is activated, install the required packages:
   - For `google-generativeai`:
     
     ```bash
     pip3 install google-generativeai
     ```
     
   - For `SpeechRecognition`:
     
     ```bash
     pip3 install SpeechRecognition
     ```
     
   - For `pyttsx3`:
     
     ```bash
     pip3 install pyttsx3
     ```
     
5. **Google Generative AI API Key and Model**

   - For API Key: Visit [Google AI Studio](https://aistudio.google.com/) to get your API key.
   - Replace the placeholder in the code with your key:
     
     ```python
     API_KEY = 'Your_API_Key'
     ```
     
   - For Model: If you want to use a different model than the default (`gemini-pro`), you can:
   - Visit the [Google AI Studio](https://aistudio.google.com/prompts/new_chat) to browse and select the model that best suits your needs.
   - Copy the model name and in your code, update the line:
     ```python
     model = ai.GenerativeModel("your-model-name")  # Replace the model name you have copied
     ```
     
   ***⚠️ Note:***
   - Google provides a free tier for Generative AI with limited monthly usage.
   - If you exceed the free quota or use premium models, charges may apply.
   - Use Responsibly, stay within free limits and avoid unexpected charges.

---

## 🚀 Usage

1. Run the script:

   ```bash
   python pytutor.py
   ```

2. Speak your Python-related question when prompted.

3. Doremon will respond with a spoken answer.

4. Say "explain in detail" or "give me more details" if you want a longer explanation.

5. Say "exit" anytime to stop the program.

---

## 🧠 Code Structure

- **`pytutor.py`**: Main script containing:
  - API configuration `google-generativeai`
  - Voice input using `speech_recognition`
  - Voice output using `pyttsx3`
  - Gemini model prompt construction and interaction
  - Voice-based command loop

---

## 🤝 Contributing

Contributions are welcome! If you'd like to suggest improvements, report bugs, or add new features, please open an issue or submit a pull request.

---

## 📬 Contact

For queries or suggestions, please contact:    
[Karthik Nandeti](mailto:karthiknandeti@gmail.com)

---

## ⚠️ Disclaimer

This project uses Google Generative AI. Make sure to follow their [terms of services](https://ai.google.dev/gemini-api/terms) when using the API.

---
