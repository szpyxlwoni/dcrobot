import discord
import os
from web3 import Web3

client = discord.Client()
w3 = Web3(Web3.HTTPProvider('https://rpc.ankr.com/eth'))

@client.event
async def on_connect():
	for channel in client.get_all_channels():
		global messageChannel
		if (channel.name == 'free_mint'):
			messageChannel = channel

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await messageChannel.send('Hello!')

token = os.getenv('TOKEN')

if (token is not None):
	client.run(token)
else:
    print('Token is None')
