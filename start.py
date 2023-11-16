# This example requires the 'message_content' intent.

import discord
import logging
from functionality.Compliments.compliments import compliment_user
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
        if message.content.startswith('$help'):
            await message.channel.send('Liste des commandes:')
        if message.channel.name == "new_features":
            await propose_feature(message.author, message.content, message.channel)
        if message.author.name in ["musta33", "AnnBolyn"]:
            await compliment_user(message.channel, message.author)
        # problème todo: le client n'as pas accès à tous les utilisateurs, c'est un problème pour get le dernier message de l'utilisateur.
    client.run(token, log_handler=handler, log_level=logging.DEBUG)


if __name__ == '__main__':
    start(BOTTOKEN)
