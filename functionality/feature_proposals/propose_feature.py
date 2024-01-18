import logging

logger = logging.getLogger(__name__)
handler = logging.FileHandler(
    filename="ressources/features.txt", encoding="utf-8", mode="a"
)
logger.addHandler(handler)
logger.setLevel(logging.INFO)


async def propose_feature(user, content, channel):
    answer = (
        f":heart: Thank you @{user} for your proposal! :heart: \n I took note of it and you'll maybe see it "
        f"being implemented sooner or later! \n "
    )
    logger.info(f"NEW_PROPOSAL !:\nUser: {user} \nProposition:{content}")
    await channel.send(answer)
