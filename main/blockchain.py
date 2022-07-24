import hashlib
import json
from time import time
from urllib.parse import urlparse
import requests

class Blockchain(object):
    def __init__(self):
        self.nodes = set()
        self.chain = []
        self.current_transactions = []
        #create a genesis block
        self.new_block(previous_hash=1, proof=100)
    
    def register_node(self, address):
        """
        Add a new node to the list of nodes
        :param address: <str> Address of node
        return None
        """
        parsed_url = urlparse(address)
        self.nodes.add(parsed_url.netloc)

    def valid_chain(self, chain):
        """
        Determine if a given blockchain is valid
        :param chain: <list> A blockchain
        :return: <bool> True if valid, False otherwise
        """

        last_block = chain[0]
        current_index = 1

        while current_index < len(chain):
            block = chain[current_index]
            print(f'{last_block}')
            print(f'{block}')
            print("\n-----------\n")

            #Check that the hash of the block is correct
            if block['previous_hash'] != self.hash(last_block):
                return False
            #check if the proof of work is correct
            if not self.valid_proof(last_block['proof'], block['proof']):
                return False
            
            last_block = block
            current_index +=1
        return True
    
    def resolve_conflicts(self):
        """
        This is our consensus algorithm, it resolves conflicts by replacing our chain with the longest one in the network
        :return: <bool> true if our chain was replaced.
        """
        neighbors = self.nodes
        new_chain = None

        #we are only looking for chains longer than ours
        max_length = len(self.chain)

        #grab and verify the chains from all the nodes in our network
        for node in neighbors:
            response = requests.get(f'http://{node}/chain')
            if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain']

                #Check if the length is longer and chain is valid
                if length> max_length and self.valid_chain(chain):
                    max_length = length
                    new_chain = chain

                #replace our chain if we discovered a new, valid chain longer than ours
                if new_chain:
                    self.chain = new_chain
                    return True
                return False

    
    def new_block(self,proof, previous_hash=None):
        #creates a new block and adds it to the chain
        """
        Create a new block in the Blockchain
        :param proof: <int> The proof given by the proof of work algorithm
        :param previous_hash: (Optional) <str> Hash of previous block
        return: <dict> New Block
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transaction': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }
        #reset the current list of transactions
        self.current_transactions =  []

        self.chain.append(block)
        return block
    
    def proof_of_work(self,last_proof):
        """
        Simple proof-of-work algorithm:
            - Find a number p' such that hash(pp') contains leading 4 zeros, where p is the previous p'
            - p is the previous proof, and p' is the new proof
            :param last_proof: <int>
            return: <int>
        """
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof +=1
        
        return proof
    
    @staticmethod
    def valid_proof(last_proof, proof):
        """
        Validates the proof: Does hash(last_proof,proof) contain 4 leading zeros?
        :params last_proof: <int> previous proof
        :param proof: <int> current proof
        return: <bool> True if correct, False if not
        """
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    def new_transaction(self, sender, recipient, amount):
        #adds a new transaction to the list of transactions
        """
        Creates a new transaction to go into the next mined block.
        :param sender: <str> Address of the sender
        :param recipient: <str> Address of the recipient
        :param amount: <int> Amount transacted
        return: <int> The index of the block that will hold this transaction
        """
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })
        return self.last_block['index'] + 1


    @staticmethod
    def hash(block):
        #Hash a block
        """
        Create a SHA-256 hash of a block
        :param block: <dict> Block
        return: <str>
        """
        #we must make sure that the dictionary is ordered, or we'll have inconsistent hashes
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        #returns the last block in the chain
        return self.chain[-1]
