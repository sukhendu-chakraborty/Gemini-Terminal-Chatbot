from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Configure Gemini with your API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize the Gemini model
model = genai.GenerativeModel("gemini-2.0-flash")

# Start a chat session (this keeps history)
chat = model.start_chat(history=[])

print("Bot: Hello! I'm your assistant. How can I help you today ?.")

# Start the conversation loop
while True:
    user_input = input("You: ")

    if user_input.lower() in ['exit', 'quit']:
        print("Bot: Goodbye!")
        break

    # Send user message and get response, preserving history
    response = chat.send_message(user_input)

    print("Bot:", response.text)


