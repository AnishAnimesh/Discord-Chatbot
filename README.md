# Discord-Chatbot

## 📌 Project Description

This project is a smart **Discord Chatbot** powered by **OpenAI’s GPT model**, built with **Python** and **discord.py**. It allows users to mention the bot in chat for instant AI-driven replies, maintains recent conversation history for context, and supports a simple `!reset` command to clear chat memory. With secure environment variable handling and robust error management, this bot is a lightweight yet powerful addition to any Discord server.

---

## ✨ Features

* AI-powered intelligent responses using OpenAI GPT.
* Maintains the last 10 messages for context-aware conversations.
* Supports `!reset` command to clear chat history.
* Integrates seamlessly with Discord for real-time interactions.
* Provides error handling and logging for stability.

---

## ⚙️ Tech Stack

| Technology                    | Purpose                                                                                    |
| ----------------------------- | ------------------------------------------------------------------------------------------ |
| **Python**                    | Core programming language for the bot.                                                     |
| **discord.py** (`>=2.3.2`)    | Connects and interacts with the Discord API (sending/receiving messages, handling events). |
| **OpenAI API** (`>=1.0.0`)    | Provides GPT-powered conversational responses.                                             |
| **python-dotenv** (`>=1.0.0`) | Loads environment variables (API keys) from a `.env` file.                                 |
| **logging (built-in)**        | Logs events, errors, and debugging information.                                            |
| **.env file**                 | Stores secrets like `OPENAI_API_KEY` and `DISCORD_TOKEN` securely.                         |

---

## 🚀 Getting Started

### Prerequisites

* Python 3.9+
* A Discord bot token
* An OpenAI API key

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/Discord-Chatbot.git
cd Discord-Chatbot

# Install dependencies
pip install -r requirements.txt

# Create .env file and add your keys
OPENAI_API_KEY=your_openai_api_key
MY_API_KEY=your_discord_bot_token

# Run the bot
python main.py
```

---

