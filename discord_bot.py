import logging
import os
import discord
import asyncio


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Set up logging for the bot
logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv("DISCORD_TOKEN")

# If token is missing, exit
if not TOKEN:
    logging.error(f"Missing required token")
    exit(1)

# Background worker function
async def background_worker():
    while True:
        logging.info("Background worker is running")
        await asyncio.sleep(30)


# Event when the bot is ready
@client.event
async def on_ready():
    try:
        logging.info(f"We have logged in as {client.user}")
        client.loop.create_task(background_worker())
        logging.info("Started background worker task")
    except Exception as e:
        logging.error(f"Error while trying to start background worker: {e}")


# Event when a message is received by the bot
@client.event
async def on_message(message):
    try:
        if message.author == client.user:
            return
    
        if message.content.lower() == 'hello':
            await message.channel.send(f"Hello {message.author.global_name}!")
            return
    
        elif message.content.lower() == 'bye':
            await message.channel.send(f"Goodbye {message.author.global_name}!")
            return
    
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        await message.channel.send(f"An error occurred while trying to process your request. Please try again later.")


# Start the bot with a token
if __name__ == '__main__':
    try:
        client.run(TOKEN)
    except Exception as e:
        logging.error(f"Error while trying to start the bot: {e}")