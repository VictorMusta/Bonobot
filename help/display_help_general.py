async def display_help(message):
    if message.content == "help":
        with open("ressources/help.txt", "r") as help_file:
            answer = ""
            answer = "".join(
                [
                    answer,
                    "Demande moi de l'aide si tu as besoin en tapant 'help' dans la plupart des channels disponibles.",
                    "Tapez '$' suivi d'un mot de la liste ci dessous pour executer une commande\n",
                ]
            )
            for line in help_file.readlines():
                answer = "".join([answer, line])
            await message.channel.send(answer)
