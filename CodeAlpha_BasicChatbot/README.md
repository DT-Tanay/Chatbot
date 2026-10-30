# CodeAlpha_BasicChatbot

**CodeAlpha Python Programming Internship - Task 4**

A simple rule-based chatbot that matches what you type against known phrases and replies with predefined answers.

## Run
```bash
python chatbot.py
```
No external libraries needed (Python 3.8+).

## Sample chat
```
You: hello
CodeBot: Hi! Nice to meet you.
You: how are you
CodeBot: I'm fine, thanks! How about you?
You: bye
CodeBot: Goodbye! Have a great day!
```

## Things to try
`hello`, `how are you`, `what is your name`, `what time is it`, `tell me a joke`, `help`, `thanks`, `bye`

Input is case-insensitive and ignores punctuation. Matching is by whole words, so "hi" will not trigger on "this".

## Concepts used
`if-elif`, functions, `while` loop, input/output, `re`
