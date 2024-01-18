async def display_shop_help(channel):
    header = ("***Bienvenue dans mon magasin!\nTu pourras y trouver chaque jours une nouvelle selection d'animaux trop pipous et refaire le plein de nouriture, médicaments, vêtements et bien plus!***\n")
    answer = "Voici la liste des mots clés disponibles dans mon magasin*:\n"
    answer += "**ton stock** : Montre les objets que j'ai en stock aujourd'hui\n"
    answer += "**motclé** : Description de la commande\n"
    answer += "**ton stock** : Montre les objets que j'ai en stock aujourd'hui\n"
    answer += "**ton stock** : Montre les objets que j'ai en stock aujourd'hui\n"
    answer += "**ton stock** : Montre les objets que j'ai en stock aujourd'hui\n"
    answer += "la présence d'un de ces mots clés dans ta phrase effectuera la commande associés, ce qui permet une discussion 'naturelle'\n"
    banner = ("\*" * len(header)) + "\n"
    answer = header + banner + answer + banner
    await channel.send(answer)
