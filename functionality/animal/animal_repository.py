from discord import Client


async def handle_animal_shop_channel(engine, message):

    text_from_player = str(message.content).lower()

    if text_from_player.startswith("bonjour"):
        await say_hello(message)

    if text_from_player.startswith("help"):
        await display_shop_help(message)

    if text_from_player.startswith("montre moi ton stock"):
        await display_stock(message)

    if text_from_player.startswith("montre moi tes animaux"):
        answer = "Voici la liste de mes petits chéri adorés:\n"
        answer += "Reviens demain pour en voir de nouveaux !\n"
        await message.channel.send(answer)


async def say_hello(message):
    text = "***Bienvenue dans mon magasin !***\n"
    banner = ("\*" * len(text)) + "\n"
    answer = banner + text + banner
    answer += " Comment vas-tu aujourd'hui?\n Demande moi de l'aide si tu as besoin en tapant 'help'"
    await message.channel.send(answer)


async def display_stock(message):
    await message.channel.send("Voici ce que j'ai en stock:")


async def display_shop_help(message):
    text = "***J'ai entendu que tu avais besoin d'aide?***\n"
    banner = ("\*" * len(text)) + "\n"
    answer = banner + text + banner
    answer += "Voici la liste des commandes disponibles dans mon magasin:\n"
    answer += "'Montre moi ton stock' : Montre les objets que j'ai en stock\n"
    await message.channel.send(answer)

