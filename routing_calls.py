from discord import Client

from functionality.animal.handle_animal_shop_channel import handle_animal_shop_channel
from functionality.compliment.compliments import compliment_user
from functionality.feature_proposals.propose_feature import propose_feature
from functionality.kitchen.handle_kitchen_channel import handle_kitchen_channel
from help.display_help_general import display_help
from help.display_not_implemented_yet import display_not_implemented_yet
from sqlalchemy import create_engine

engine = create_engine(
    "mysql+mysqlconnector://u39524_cFA7dtFzsk:QNMlWSPg8!Af!SIQTxXiNC63@161.97.78.70:3306/s39524_BonoBot"
)


async def on_message(client: Client, message):
    if message.author == client.user:
        return

    if message.content.startswith("$ping"):
        await message.channel.send("PONG!")

    if message.channel.name == "magasin":
        await handle_animal_shop_channel(engine, message)

    if message.channel.name == "new_features":
        await propose_feature(message.author, message.content, message.channel)

    if message.content == "help" and message.channel.name == "général":
        await display_help(message)

    if message.channel.name == "cuisine":
        await handle_kitchen_channel(message)

    if message.content.startswith("$recette"):
        await display_not_implemented_yet(message.channel)

    if message.author.name in ["AnnBolyn", "$waggLord", "Ashino", "mameloukk", "musta33"]:
        await compliment_user(message.channel, message.author)

    # TODO: faire en sorte que le bot ai accès aux utilisateurs. (que le bot dans client.get_all_users())
