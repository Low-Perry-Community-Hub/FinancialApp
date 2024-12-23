from web3 import Web3

w3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"))

def get_wallet_balance(wallet_address):
    balance = w3.eth.get_balance(wallet_address)
    return {"address": wallet_address, "balance_eth": w3.fromWei(balance, 'ether')}
