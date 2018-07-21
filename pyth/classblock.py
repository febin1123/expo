import time
 
class head:
    def __init__(self,id,prev_id,count):
        self.id = id
        self.prev_id = prev_id
        self.count = count
 
class tail:
    def __init__(self,next_id):
        self.next_id = next_id
        self.modified() # for the last modified time
    def modified(self):
        # function must be called everytime the block is accessed
        # EVERYTIME!
        self.last_modified = time.time()
 
class timestamp:
    # timestamp of the date of creation
    def __init__(self):
        self.timestamp = time.time()
 
class body:
    # contains a LIST of transactions
    def __init__(self,transactions):
        self.transactions = transactions
 
class block:
    # a block conisting of
    # head | body | timstamp | tail
    def __init__(self,head,body,timestamp,tail):
        self.head = head
        self.body = body
        self.timestamp = timestamp
        self.tail = tail
 
class chain:
    blockchain = [] # will contain a list of blocks
 
    def input_transactions(self):
        # Taking input of transactions, making a list
        # and return the list, and count of transactions
        n = int(input('Number of transactions?: ')) # count of transactions
        transactions=[] # list of transactions
        for i in range(n):
            print('Transactions #',(i+1))
            name = input('Name?: ')
            amount = input('Amount?:')
            transactions.append({name,amount})
        return n,transactions
 
    def modify_tail(self,tail,next_id):
        # This function needs to be called everytime a new block is added
        # Modifies the tail part of the PREVIOUS block in the chain
        tail.next_id = next_id
        tail.modified() # called because the block was accessed
 
    def create_block(self):
        # Creating the head part
        head_id = ''
        prev_id = ''
        if(len(self.blockchain)==0): # if the block is the first block
            head_id = 'id001'
            prev_id = None
        else: # for subsequent blocks in the chain
            head_id = 'id00'+str(len(self.blockchain)+1)
            prev_id = 'id00'+str(len(self.blockchain))
            self.modify_tail(self.blockchain[-1].tail,head_id) # tail of the previous block in the chain needs to be modified
        count, transactions = self.input_transactions() #fetching the count + transactions
        #Creating objects for each of the sub parts inside a block
        next_head = head(head_id,prev_id,count)
        next_body = body(transactions)
        next_timestamp = timestamp()
        next_tail = tail(None)
        # Creating a block
        next_block = block(head=next_head, body=next_body, timestamp=next_timestamp, tail=next_tail)
        # adding block to blockchain LIST
        self.blockchain.append(next_block)
 
    def show_all(self):
        # Iterating through all the blocks in the blockchain LIST
        # displaying all the data individually
        # Modify the display part as you wish
        for items in self.blockchain:
            print('Head\n--------')
            print('[ ',items.head.id,' | ',items.head.prev_id,' | ',items.head.count,' ]')
            print('Body\n--------')
            print('[ ',items.body.transactions,' ]')
            print('Timestamp\n--------------')
            print('[ ',items.timestamp.timestamp,' ]')
            print('Tail\n------------')
            print('[ ',items.tail.next_id,' | ',items.tail.last_modified,' ]')
 
 
# Creating a chain OBJECT
bc = chain()
no_of_blocks = input('Number of blocks?: ')
for iteration in range(no_of_blocks):
    bc.create_block()
# Showing the entire blockchain
bc.show_all()