class DynamicArray:
    def __init__(self, arr):
        self.data = arr
        self.length = len(self.data)

    def __str__(self):
        x = "[ "
        for i in self.data:
            x += str(i)+" "
        x += "]"
        return x
    
    def __len__(self):
        return len(self.data)
    
    def cusprint(self):
        print('['+''.join(' {} '.format(i) for i in self.data)+']')
    
    def append(self, data):
        self.data.append(data)
        
    def insertAt(self,data,pos):
        if pos<0 or pos> self.length:
            print("Out of Index")
        else:
            temp1 = self.data[:pos]
            temp2 = self.data[pos:]
            inserted_data = [data]
            self.data = temp1+inserted_data+temp2
            
    
    def pop(self,pos = None):
        if pos is not None:
            if pos<0 or pos>self.length:
                print("out of Index")
            else:
                del self.data[pos]
        else:
            del self.data[-1]
    
    def extend(self, data):
        for i in data:
            self.data.append(i)
    
    def clear(self):
        self.data = []
        