class queue:
    def __init__(self, data):
        self.data = data
    
    def enqueue(self,data):
        self.data.append(data)
    
    def dequeue(self):
        self.data.pop(0)
    
    def __len__(self):
        return len(self.data)
    
    def __str__(self):
        return (''.join('{}||'.format(i) for i in self.data))
    
    def head(self):
        return self.data[0]
    
    def tail(self):
        return self.data[-1]