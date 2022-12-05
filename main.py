import discord
import codex
import os
import dotenv
import keep_alive

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

dotenv.load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")


@client.event
async def on_ready():
    print("Bot is ready")


@client.event
async def on_message(message):
    # Check if the message was sent in the correct channel
    if message.channel.id == 1049433960905711646:
        # Check if the bot was mentioned in the message
        if client.user in message.mentions:
            # Generate a response using the codex.ask method
            answer = codex.ask(message.content)

            if answer:
                # Send the response to the channel
                await message.channel.send(answer)

keep_alive.keep_alive()
client.run(BOT_TOKEN)
