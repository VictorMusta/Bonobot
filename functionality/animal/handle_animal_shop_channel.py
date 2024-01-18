from help.display_help_shop import display_shop_help


async def handle_animal_shop_channel(engine, message):
    header_from_player = str(message.content).lower()

    if header_from_player.startswith("bonjour"):
        await say_hello(message)

    if header_from_player.startswith("help"):
        await display_shop_help(message.channel)

    if header_from_player.__contains__("ton stock"):
        await display_stock(message)

    if header_from_player.startswith("montre moi tes animaux"):
        answer = "Voici la liste de mes petits chéri adorés:\n"
        answer += "Reviens demain pour en voir de nouveaux !\n"
        await message.channel.send(answer)


async def say_hello(message):
    header = "***Bienvenue dans mon magasin !***\n"
    banner = ("\*" * len(header)) + "\n"
    answer = banner + header + banner
    answer += " Salut toi!\n"
    answer += " Comment vas-tu aujourd'hui?\n"
    await message.channel.send(answer)


async def display_stock(message):
    await message.channel.send("Voici ce que j'ai en stock:")



