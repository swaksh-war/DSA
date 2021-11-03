class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value 
        self.next = None
        
class hashtable:
    def __init__(self,size=10):
        self.values = [None]*size
    
    def hashkey(self,key):
        return key % 10
    
    def datainsert(self,key,value):
        address = self.hashkey(key)
        self.values[address] = value
        if self.values.index(address) is not None:
            ko

    def printht(self):
        for i in self.values:
            if i is not None:
                print(f'key : {self.values.index(i)} and value(s): {i}')

ht = hashtable()
ht.datainsert(2,'ankit')
ht.printht()
        