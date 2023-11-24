from functionality.Compliments.compliments import compliment_user
from functionality.feature_proposals.propose_feature import propose_feature
from functionality.help.display_help import display_help
from functionality.help.display_not_implemented_yet import display_not_implemented_yet


async def on_message(client, message):

    if message.author == client.user:
        return

    if message.content.startswith('$help'):
        await display_help(message)

    if message.content.startswith('$recette'):
        await display_not_implemented_yet(message.channel)

    if message.channel.name == "new_features":
        await propose_feature(message.author, message.content, message.channel)

    if message.author.name in ["AnnBolyn"]:
        await compliment_user(message.channel, message.author)

    # TODO: faire en sorte que le bot ai accès aux utilisateurs. (que le bot dans client.get_all_users())
