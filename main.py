import discord
import os
from web3 import Web3
import requests
import codecs

client = discord.Client()
web3 = Web3(Web3.HTTPProvider('https://rpc.ankr.com/eth'))
baseUrl = 'https://raw.githubusercontent.com/ethereum-lists/4bytes/master/signatures/'

blockNumber = web3.eth.get_block_number()
print(blockNumber)
transCount = web3.eth.get_block_transaction_count(blockNumber)
for index in range(transCount):
    transaction = web3.eth.get_transaction_by_block(blockNumber, index)
    if (transaction.to != None and transaction.input != '0x'):
        # contract = web3.eth.contract(transaction.to)
        # result = requests.get(baseUrl + transaction.input[2:10])
        try:
            f = codecs.open('./signatures/' + transaction.input[2:10], 'r', 'utf-8')
        except IOError:
        	f.close()
        else:
        	print(f.read())
        	f.close()

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
	# client.run(token)
	print(111)
else:
    print('Token is None')
