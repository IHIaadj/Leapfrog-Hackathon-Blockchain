#!flask/bin/python

import json
import time
from BlockChain import Blockchain
import wallet
from Good import Land, Vehicle 
from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__)

blockchain = Blockchain()
users = []
currentUser = 0
walletAlice = wallet.Wallet([Vehicle(1,1,53451162589,"red", "wolkswagen")], [Land(1,37,38,"29 rue parc dounia" ,[(37.01,38.002), (37.2,36,2) ],100, 1), Land(2,37,38,"28 rue parc dounia" ,[(37.01,38.002), (37.2,36,2) ],200, 2)])
walletBob = wallet.Wallet([], [Land(1,37,38,"29 rue parc dounia" ,[(37.01,38.002), (37.2,36,2) ],400,0)])
@app.route('/login', methods=['POST'])
def login(): 
    login_data = request.get_json()
    required_fields = ["email", "password"]

    for field in required_fields:
        if not login_data.get(field):
            return "Invlaid login data", 404
    
    user = ["alice@smartcity.com", "bob@smartcity.com"]
    password = "password"

    if (login_data['email'] not in user):
        return "fail"
    if (login_data['password'] != "password"):
        return "fail"
  
    global currentUser
    currentUser = login_data['email'].split('@')[0]
    return "success"


@app.route('/wallet', methods=['GET'] )
def wallet():
    if (currentUser == 0 ):
        return 'fail'
    if(currentUser == 'alice') :
        return walletAlice.toJSON()
    else :
        return walletBob.toJSON()

@app.route('/unconfirmed_transations', methods=['GET'])
def get_undefined_transactions():
    return jsonify({'trans': blockchain.unconfirmed_transactions})


@app.route('/new_transaction', methods=['POST'])
def new_transaction():
    tx_data = request.get_json()
    required_fields = ["sender", "receiver", "good", "notaire"]
 
    for field in required_fields:
        if not tx_data.get(field):
            return "Invlaid transaction data", 404
 
    tx_data["timestamp"] = time.time()
 
    blockchain.add_new_transaction(tx_data)
 
    return "Success\n", 201

@app.route('/chain', methods=['GET'])
def get_chain():
    chain_data = []
    for block in reversed(blockchain.chain):
        chain_data.append(block.__dict__)
    bChain = [{"length": len(chain_data)},{"chain": chain_data}]
    return jsonify({'blockchain': bChain})

@app.route('/mine', methods=['GET'])
def mine_unconfirmed_transactions():
    result = []
    result = blockchain.mine()
    if not result:
        return "No transactions to mine"
    return jsonify({'mined': result})

if __name__ == '__main__':
    app.run(debug=True)