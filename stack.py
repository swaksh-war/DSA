class Stack:
    def __init__(self, data):
        self.data = data
    
    def push(self, data):
        self.data.insert(0,data)
    
    def pop(self):
        return self.data.pop(0)
    
    def top(self):
        return self.data[0]
    
    def __len__(self):
        return len(self.data)
    
    def __str__(self):
        return (''.join('{}\n'.format(i) for i in self.data))