from random import randint


async def compliment_user(channel, user_name):
    with open("ressources/compliments.txt") as compliment_file:
        compliments = compliment_file.readlines()
        answer = compliments[randint(0, len(compliments) - 1)].format(user_name)
        await channel.send(answer)