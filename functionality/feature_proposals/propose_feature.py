import logging

logger = logging.getLogger('proposalLogger')
handler = logging.FileHandler(filename='features.log', encoding='utf-8', mode='w')
logger.addHandler(handler)
logger.setLevel(logging.INFO)


async def propose_feature(user, content, channel):
    answer = (f':heart: Thank you @{user} for your proposal! \n I took note of it and you\'ll maybe see it '
              f'being implemented sooner or later! :heart: \n ')
    logger.info(f'NEW_PROPOSAL !:\nUser: {user} \nProposition:{content}')
    await channel.send(answer)
