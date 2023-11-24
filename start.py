
import discord
import logging
import os
import calls
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.


def start(token):
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
    logger = logging.getLogger("__name__")
    logger.addHandler(handler)

    print('BonoBot in action!')

    @client.event
    async def on_ready():
        print(f'We have logged in as {client.user}')

    @client.event
    async def on_message(message):
        await calls.on_message(client, message)
    client.run(token, log_handler=handler, log_level=logging.DEBUG)


if __name__ == '__main__':
    start(os.environ['BOTTOKEN'])
