"""
CodeAlpha Python Programming Internship
Task 4: Basic Chatbot

A simple rule-based chatbot. It reads what the user types, looks for known
phrases (hello, how are you, bye, ...) and answers with a predefined reply.

Concepts used: if-elif, functions, loops, input/output.
"""

import re
from datetime import datetime

BOT_NAME = "CodeBot"


def normalize(text):
    """Lowercase the text and strip punctuation so matching is forgiving."""
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s']", " ", text)
    return " ".join(text.split())


def contains(text, *phrases):
    """
    True if any phrase appears in text as whole words.
    (So 'hi' matches 'hi there' but NOT 'this'.)
    """
    padded = f" {text} "
    return any(f" {phrase} " in padded for phrase in phrases)


def get_response(user_input):
    """
    Return (reply, should_exit) for the user's message.
    Rules are checked from top to bottom; the first match wins.
    """
    text = normalize(user_input)

    if text == "":
        return "Please type something and I'll do my best to answer.", False

    elif contains(text, "bye", "goodbye", "exit", "quit", "see you"):
        return "Goodbye! Have a great day!", True

    elif contains(text, "how are you", "how are you doing", "how r u", "how do you do"):
        return "I'm fine, thanks! How about you?", False

    elif contains(text, "i am fine", "i'm fine", "i am good", "i'm good",
                  "i am great", "i'm great", "doing well"):
        return "Glad to hear that!", False

    elif contains(text, "hello", "hi", "hey", "good morning",
                  "good afternoon", "good evening"):
        return "Hi! Nice to meet you.", False

    elif contains(text, "your name", "who are you"):
        return f"I'm {BOT_NAME}, a simple Python chatbot.", False

    elif contains(text, "what can you do", "help"):
        return ("I can chat about simple things. Try: 'hello', 'how are you', "
                "'what is your name', 'what time is it', 'tell me a joke' or 'bye'."), False

    elif contains(text, "time"):
        return f"The current time is {datetime.now():%I:%M %p}.", False

    elif contains(text, "date", "today"):
        return f"Today's date is {datetime.now():%A, %d %B %Y}.", False

    elif contains(text, "joke"):
        return "Why do programmers prefer dark mode? Because light attracts bugs!", False

    elif contains(text, "thanks", "thank you"):
        return "You're welcome!", False

    else:
        return "Sorry, I didn't understand that. Type 'help' to see what I can do.", False


def main():
    print("=" * 50)
    print(f"  {BOT_NAME} - a simple rule-based chatbot")
    print("  Type 'bye' to end the chat.")
    print("=" * 50)

    while True:
        user_input = input("\nYou: ")
        reply, should_exit = get_response(user_input)
        print(f"{BOT_NAME}: {reply}")

        if should_exit:
            break


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\nProgram closed. Goodbye!")
