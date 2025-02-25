import hashlib
import time

# Block Class
class Block:
    def __init__(self, index, previous_hash, data, nonce=0):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def __str__(self):
        return f"Block {self.index} [Hash: {self.hash}, Previous Hash: {self.previous_hash}, Data: {self.data}, Nonce: {self.nonce}]"

# Blockchain Class
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4  # Difficulty for Proof of Work

    def create_genesis_block(self):
        return Block(0, "0", "Genesis Block")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.proof_of_work(new_block)
        self.chain.append(new_block)

    def proof_of_work(self, block):
        target = '0' * self.difficulty
        while block.hash[:self.difficulty] != target:
            block.nonce += 1
            block.hash = block.calculate_hash()
        print(f"Block mined: {block.hash}")

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                print("Current block hash is invalid!")
                return False

            if current_block.previous_hash != previous_block.hash:
                print("Previous block hash is invalid!")
                return False

        return True

# Testing the Blockchain
if __name__ == "__main__":
    my_blockchain = Blockchain()

    print("Mining block 1...")
    my_blockchain.add_block(Block(1, "", "Transaction Data 1"))

    print("Mining block 2...")
    my_blockchain.add_block(Block(2, "", "Transaction Data 2"))

    print("Mining block 3...")
    my_blockchain.add_block(Block(3, "", "Transaction Data 3"))

    # Print the blockchain
    print("\nBlockchain:")
    for block in my_blockchain.chain:
        print(block)

    # Validate the blockchain
    print("\nIs blockchain valid?", my_blockchain.is_chain_valid())