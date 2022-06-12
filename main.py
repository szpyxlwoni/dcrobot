import discord
import os
from web3 import Web3
import codecs
import requests

client = discord.Client()
web3 = Web3(Web3.HTTPProvider('https://rpc.ankr.com/eth'))
dictMap = {}
etherScanUrl = 'https://api.etherscan.io/api?module=contract&action=getsourcecode&apikey=' + os.getenv('ESAPIKEY')

try:
    f = codecs.open('./signature', 'r', 'utf-8')
except IOError:
	f.close()
else:
	for line in f:
		keyValue = line.split('=')
		dictMap[keyValue[0]] = keyValue[1]
	
	f.close()

@client.event
async def on_connect():
	for channel in client.get_all_channels():
		global messageChannel
		if (channel.name == 'free_mint'):
			messageChannel = channel

	blockNumber = web3.eth.get_block_number()
	transactions = web3.eth.get_block(blockNumber, True).transactions
	for transaction in transactions:
	    if (transaction.to != None and transaction.input != '0x'):
	    	key = transaction.input[2:10]
	    	if (key in dictMap):
	            if ('mint' in dictMap[key] and transaction.value == 0):#增加logs判定
	            	# messageChannel.send('free mint=' + transaction.to)
	            	requests.get('')

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
