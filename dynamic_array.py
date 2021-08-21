import ctypes

class DynamicArray(object):
    def __init__(self):
        self.length = 0
        self.capacity = 1
        self.Arr = self.make_array(self.capacity)
    
    def make_array(self, n):
        return (n *ctypes.py_object)()
    
    def __len__(self):
        return self.length
    
    def __getitem__(self, k):
        if not 0 <= k < self.length:
            return IndexError('Out Of Bound')
        return self.Arr[k]
    def _resize(self, n):
        b = self.make_array(n)
        for k in range(n):
            b[k] = self.Arr[k]
        self.Arr = b
        self.capacity = n
    
    def append(self, elem):
        if self.length == self.capacity:
            self._resize(2 * self.capacity)
            self.Arr[self.length] = elem
            self.length += 1
    
    def insertAt(self,item, index):
        if index<0 or index>self.length:
            print ("out of index")
            return
        if self.length == self.capacity:
            self._resize(2*self.capacity)
        for i in range(self.length-1, index-1, -1):
            self.Arr[i+1] = self.Arr[i]
        
        self.Arr[index] = item
        self.length +=1
    
    def delete(self):
        if self.length == 0:
            print("Array is already empty")
            return
        self.Arr[self.length-1] = 0
        self.n-=1
    
    def removeAt(self,index):
        if self.length == 0:
            print("Array is already empty")
            return
        if index<0 or index > self.length:
            return IndexError("Out of Index")
        
        if index==self.length -1:
            self.Arr[index]=0
            self.length -= 1
            return
        for i in range(index, self.length-1):
            self.Arr[i] = self.Arr[i+1] 