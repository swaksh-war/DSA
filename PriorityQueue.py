from QuickSort import quick_sort
class Priorityqueue:
    def __init__(self,data=None):
        self.data = data
        self.len = len(self.data)
    
    def __str__(self):
        quick_sort(self.data, 0, len(self.data)-1)
        return ('['+''.join(' {} '.format(i) for i in self.data)+']')
    
    def __len__(self):
        return len(self.data)
    
    def poll(self):
        self.data.pop(0)
        quick_sort(self.data, 0, len(self.data)-1)
        return self.data
    
    def insert(self, elem):
        self.data.append(elem)
        quick_sort(self.data, 0, len(self.data)-1)
        return self.data
    
    def remove(self, elem):
        if elem not in self.data:
            print("{} isn't in the given queue".format(elem))
        else:
            self.data.remove(elem)
        
        quick_sort(self.data, 0, len(self.data)-1)
        return self.data
    
    def position(self, elem):
        if elem not in self.data:
            self.data.append(elem)
        quick_sort(self.data, 0,  len(self.data)-1)
        
        return self.data.index(elem)
    