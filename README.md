# Telegram Bot: Voice Message Summarizer

## Overview

This Telegram bot uses AI (powered by Sber GigaChat) to process voice messages and provide concise summaries of the main
ideas. You can:

Chat with the bot directly by sending it a voice message.

Add the bot to group chats where it can summarize voice messages for everyone :)

## Features

Voice Message Summarization: Converts voice messages into text and extracts the most important ideas.

Group Chat Integration: Works in group conversations to summarize voice messages shared by members.

AI-Powered: Utilizes Sber GigaChat for accurate and contextual understanding.

User-Friendly: Simple and intuitive commands for easy interaction.

## How to Use

* Direct Chat

    * Start a chat with the bot by clicking on its username.

    * Send a voice message to the bot.

    * Receive a text summary of the message.

* Group Chat

    * Add the bot to your group.

    * Share a voice message in the group.

    * The bot will automatically reply with a summary of the voice message.

## Commands

* **/start**: Begin interaction with the bot and learn about its features.

* **/help**: Get detailed instructions on using the bot.

## For Developers

Code structure:

```
VoiceSummaryBot/
├── bot/
│   ├── __init__.py          
│   ├── config.py            
│   ├── handlers/
│   │   ├── __init__.py      
│   │   ├── start.py         
│   │   ├── ai_interaction.py
│   │   ├── fallback.py      
│   └── keyboards.py         
├── ai/
│   ├── __init__.py          
│   ├── gigachat_client.py   
│   ├── processing.py        
│   └── prompts.py           
├── utils/
│   ├── __init__.py          
│   ├── database.py          
│   ├── logging.py           
│   └── helpers.py           
├── requirements.txt         
├── .env                     
├── main.py                  
├── README.md                
└── LICENSE                  

```

Clone this repository:

`git clone https://github.com/MattoYuzuru/VoiceSummaryBot`

Navigate to the project directory:

`cd VoiceSummaryBot`

Install dependencies:

`pip install -r requirements.txt`

Create a .env file and add the following variables:

```
BOT_TOKEN=your-telegram-bot-token
GIGACHAT_API_KEY=your-gigachat-api-key
```

Run the bot:

`python main.py`

**Feel free to contribute or provide feedback to make this bot even better!**

