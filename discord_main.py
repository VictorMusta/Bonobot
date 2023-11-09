# This example requires the 'message_content' intent.

import discord
import logging
from functionality.feature_proposals.propose_feature import propose_feature


def start(token):

    intents = discord.Intents.default()
    intents.message_content = True

    client = discord.Client(intents=intents)
    handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
    logger = logging.getLogger("__name__")
    logger.addHandler(handler)
    # Assume client refers to a discord.Client subclass...

    @client.event
    async def on_ready():
        print(f'We have logged in as {client.user}')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        print(message)
        print(message.channel.name)
        if message.content.startswith('$'):
            await message.channel.send('Hello!')
        if message.channel.name == "new_features":
            await propose_feature(message.author, message.content, message.channel)
        await message.channel.send('t\'m! :cat:')

    client.run(token, log_handler=handler, log_level=logging.DEBUG)
