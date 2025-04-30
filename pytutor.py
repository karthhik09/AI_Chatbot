import google.generativeai as ai
import speech_recognition as sr
import pyttsx3

API_KEY = 'AIzaSyA-kyCjsLOyTYRKkbgO-VOveuffLQixzuk'
ai.configure(api_key=API_KEY)
model = ai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat()

# Default prompt
default_prompt = "You are Doremon, a friendly Python tutor. Provide concise Python programming answers. Don't use emojis. Be interactive."

# Initialize the recognizer and TTS engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

# Function to listen to user input
def listen():
    with sr.Microphone() as source:
        print("Doremon: Listening... Speak clearly.")
        speak("Listening... Speak clearly.")
        recognizer.adjust_for_ambient_noise(source)

        try:
            audio = recognizer.listen(source, timeout=15, phrase_time_limit=30)
            text = recognizer.recognize_google(audio).lower()
            print(f"Doremon: You said: {text}")
            return text
        except (sr.WaitTimeoutError, sr.UnknownValueError, sr.RequestError):
            print("Doremon: I couldn't hear or understand you. Try again.")
            speak("I couldn't hear or understand you. Try again.")
            return None

# Function to speak a response
def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

# Function to inform the user that the system is processing information
def processing_info():
    print("Doremon: I'm processing your request, please wait...")
    speak("I'm processing your request, please wait...")

# Chatbot loop
print("Doremon Python Tutor started. Say 'exit' to stop.")
speak("Doremon Python Tutor started. Say 'exit' to stop.")
while True:
    user_input = listen()

    if user_input:
        if "exit" in user_input:
            print("Doremon: Exiting Python Tutor...")
            speak("Goodbye! Keep coding!")
            break

        # Check if the user wants a detailed explanation
        if "explain in detail" in user_input or "give me more details" in user_input:
            modified_prompt = "Provide a detailed explanation of Python concepts."
        else:
            modified_prompt = default_prompt  # Default response

        # Inform the user that Doremon is processing the request
        processing_info()

        # Send modified prompt + user input to API
        response = chat.send_message(f"{modified_prompt}\nUser: {user_input}")
        
        # Chatbot response
        bot_response = response.text
        print(f"Doremon: {bot_response}")
        speak(bot_response)
