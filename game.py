from web3 import Web3

web3 = Web3(Web3.WebsocketProvider('wss://ropsten.infura.io/ws/v3/62bf1ec2f8f347a2b2f003f1eb94f90b'))

web3.eth.default_account = '0x26Bf6130486E08E16EEF106cA15470d78e5B869E'

signed_txn = web3.eth.account.sign_transaction({
	'nonce': web3.eth.get_transaction_count('0x26Bf6130486E08E16EEF106cA15470d78e5B869E'),
	'maxFeePerGas': 3000000000,
    'maxPriorityFeePerGas': 2000000000,
    # 'from': '0x26Bf6130486E08E16EEF106cA15470d78e5B869E',
	'to': '0xEb7ab20Bd1De930d12321841597E4c93D9d33bfB',
	'value': web3.toWei(1, 'ether'),
	'gas': 50000,
    'data': '0x4ba4c16b0000000000000000000000000000000000000000000000000000000000000001',
    'chainId': 3
},
'ceb41d11d99b116197c3816378d21243ca3afc5d317a0ed5216992bdc42cd490')

# print(web3.eth.get_block(12411322).timestamp)
# print(web3.toHex(web3.eth.get_storage_at('0xEb7ab20Bd1De930d12321841597E4c93D9d33bfB', 0)))
# print(web3.toHex(web3.solidityKeccak(['bytes', 'uint256'], ['0x01012c5e09cc2c7341e48d13e153abf499479d7d1decb640279338ac6bb1ab5d', 1655450568])))

web3.eth.send_raw_transaction(signed_txn.rawTransaction)