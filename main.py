import discord
import os
import logging
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DISCORD_TOKEN = os.getenv("MY_API_KEY")

if not OPENAI_API_KEY or not DISCORD_TOKEN:
    raise EnvironmentError("Missing OPENAI_API_KEY or MY_API_KEY in environment variables.")

openai_client = OpenAI(api_key=OPENAI_API_KEY)

# Store conversation history per channel
chat_history = {}
MAX_HISTORY = 10  # Limit history to last 10 messages

class MyClient(discord.Client):
    async def on_ready(self):
        logging.info(f'Bot logged in as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user:
            return

        # Reset command
        if message.content.strip().lower() == "!reset" and self.user in message.mentions:
            chat_history.pop(str(message.channel.id), None)
            await message.channel.send("Chat history reset!")
            return

        if len(message.mentions) == 1 and self.user in message.mentions:
            channel_id = str(message.channel.id)
            chat_history.setdefault(channel_id, [])

            user_message = message.content.replace(f"<@{self.user.id}>", "").strip()
            if not user_message:
                await message.channel.send("Please ask something after mentioning me!")
                return

            chat_history[channel_id].append({"role": "user", "content": user_message})
            # Keep only the last MAX_HISTORY messages
            chat_history[channel_id] = chat_history[channel_id][-MAX_HISTORY:]

            try:
                async with message.channel.typing():
                    response = openai_client.chat.completions.create(
                        model="gpt-3.5-turbo",
                        messages=chat_history[channel_id],
                        max_tokens=256
                    )
                    reply = response.choices[0].message.content.strip()
                    chat_history[channel_id].append({"role": "assistant", "content": reply})
                    chat_history[channel_id] = chat_history[channel_id][-MAX_HISTORY:]
                    await message.channel.send(reply)
            except Exception as e:
                logging.error(f"Error: {e}")
                await message.channel.send(f"Sorry, I encountered an error: {e}")

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(DISCORD_TOKEN)