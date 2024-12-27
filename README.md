# Python Chatbot

This repository contains a simple Python-based chatbot that responds to predefined messages. The chatbot uses a dictionary of rules where each keyword is associated with a response. It processes user input, searches for matching keywords, and returns the appropriate response. If no match is found, it prompts the user to repeat their message.

## Features

- Responds to various greetings and questions.
- Handles multiple messages, including greetings like "Hello", "Good morning", and "Good night".
- Offers predefined responses to questions about its identity, programming, and other topics.
- Can tell jokes and share fun facts.
- Users can exit the chat by typing "exit".

## How It Works

The chatbot listens to the user's input, compares it to a set of predefined rules, and responds accordingly. If no match is found, it will ask the user to repeat their message.

## Requirements

- Python 3.x

No additional libraries are required to run this chatbot.

## How to Use

1. Clone or download this repository.
2. Open the script in any Python IDE or text editor.
3. Run the script.
4. Interact with the chatbot by typing your messages.
5. Type "exit" to end the conversation.

## Code Breakdown

- **`regras` Dictionary**: Contains keyword-response pairs. Each keyword is mapped to a specific response.
- **`chatbot_resp` Function**: Takes a user input message, converts it to lowercase, and checks it against the keywords in the `regras` dictionary. If a match is found, it returns the corresponding response.
- **Main Loop**: The main loop waits for user input and continues until the user types "exit".

## Customizing the Chatbot

You can modify the responses by updating the `regras` dictionary. Add new keywords and responses to make the chatbot more interactive or tailored to your needs.
