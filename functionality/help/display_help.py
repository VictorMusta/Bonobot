
async def display_help(message):
    if message.content == "$help":
        with open("ressources/help.txt", "r") as help_file:
            answer = ""
            answer = "".join([answer, "Tapez '$' suivi d'un mot de la liste ci dessous pour executer une commande\n"])
            for line in help_file.readlines():
                answer = "".join([answer, line])
            await message.channel.send(answer)

