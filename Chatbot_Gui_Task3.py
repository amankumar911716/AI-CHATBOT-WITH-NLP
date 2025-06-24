import nltk
import random
import string
import tkinter as tk
from tkinter import scrolledtext
from nltk.stem import WordNetLemmatizer

# Download NLTK resources (first time only)

nltk.download('punkt')
nltk.download('wordnet')

# Initialize Lemmatizer

lemmatizer = WordNetLemmatizer()

# Knowledge base

faq_pairs = {
    "what is your name": "I am a chatbot created using Python and NLTK.",
    "how are you": "I'm just a bot, but I'm doing great!",
    "what is nlp": "NLP stands for Natural Language Processing.",
    "what can you do": "I can chat with you and answer some simple questions.",
    "bye": "Goodbye! Have a great day!",
}

user_greetings = ["hello", "hi", "hey", "yo", "greetings"]
bot_greetings = ["Hello!", "Hi there!", "Hey!", "Greetings!"]

# Preprocessing

def clean_text(text):
    text = text.lower()
    text = ''.join([ch for ch in text if ch not in string.punctuation])
    tokens = nltk.word_tokenize(text)
    return [lemmatizer.lemmatize(word) for word in tokens]

# Generate chatbot response

def generate_response(user_input):
    user_input = user_input.lower()

    # Greeting response

    for word in user_input.split():
        if word in user_greetings:
            return random.choice(bot_greetings)

    # FAQ matching

    for question in faq_pairs:
        if question in user_input:
            return faq_pairs[question]

    return "I'm not sure how to respond to that. Try asking something else."

# -------------------------
# GUI with Tkinter
# -------------------------

def send_message():
    user_msg = user_input.get()
    if user_msg.strip() == "":
        return

    chat_window.insert(tk.END, f"You: {user_msg}\n")
    user_input.delete(0, tk.END)

    response = generate_response(user_msg)
    chat_window.insert(tk.END, f"Bot: {response}\n\n")

# Create main window

root = tk.Tk()
root.title("NLP Chatbot")
root.geometry("500x500")

# Chat display area

chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD)
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
chat_window.insert(tk.END, "Bot: Hello! Ask me anything...\n\n")

# User input field

user_input = tk.Entry(root, font=("Arial", 14))
user_input.pack(padx=10, pady=5, fill=tk.X)
user_input.focus()

# Send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(pady=5)

# Bind Enter key to send message

root.bind('<Return>', lambda event: send_message())

# Start GUI loop

root.mainloop()
