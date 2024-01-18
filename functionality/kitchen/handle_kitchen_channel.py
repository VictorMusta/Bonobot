from help.display_kitchen_help_message import display_kitchen_help_message


async def handle_kitchen_channel(message):
    if message.content == 'help':
        await display_kitchen_help_message(message.channel)
