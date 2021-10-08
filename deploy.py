from solcx import compile_standard, install_solc
from web3 import Web3
import json
with open('./Web3.sol', 'r') as file:
    web3 = file.read()
    compiled_sol = compile_standard(
        {
            "language": "Solidity",
            "sources": {"Web3.sol": {"content": web3}},
            "settings": {
                "outputSelection": {
                    "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
                }
            },
        },
        solc_version="0.6.0",
    )
with open('compiled_sol.json','w') as file:
    json.dump(compiled_sol,file)

bytecode = compiled_sol["contracts"]['Web3.sol']['Web3']["evm"]["bytecode"]['object']
abi = compiled_sol["contracts"]['Web3.sol']['Web3']['abi']
w3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))
chainId = 1337
myAddress = "0xEe323b617Ff465515E42fe5029b2C41d925E220c"
private_key = '0x3d1c7f3ade16acf3a92b45eada62306ebc436a94fc4258cd48f75e6613c46ca8'

web3 = w3.eth.contract(abi=abi,bytecode=bytecode)
nonce = w3.eth.getTransactionCount(myAddress)

transaction = web3.constructor().buildTransaction({"chainId":chainId,"from":myAddress,"nonce":nonce})
print(transaction)



































