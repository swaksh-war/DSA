class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self,head=None,tail=None):
        self.size = 0
        self.head = head
        self.tail = tail
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        x = self.head
        toprint=[]
        while(x!=None):
            toprint.append(x.data)
            x = x.next
        return ('['+''.join(f' {i} ' for i in toprint)+']')            
    
    def clear(self):
        x = self.head
        if self.size !=0:
            while(x != None):
                next = x.next
                x.data = None
                x = next
            self.size = 0
            
        elif self.size ==0:
            Exception("The LinkedList is already cleared")
    
    def emptyCheck(self):
        if self.size == 0:
            return True
        return False
    
    def addBegin(self, data):
        
        if self.size == 0:
            node  = Node(data)
            self.head = node
            self.tail = node

        else:
            node = Node(data)
            node.next = self.head
            self.head = node
        self.size+=1
    
    def addAfter(self,data,index):

        if index == 0:
            self.addBegin(data)

        elif index<0:
            raise IndexError("Minimum value must be 0 referred to the begining of the LinkedList")

        else:
            node = Node(data)

            x = self.head
            i = 0
            while(i!=index):
                if(x!=None):
                    x = x.next
                    i+=1

            if (x!= None):
                node.next = x.next
                x.next = node
        self.size+=1
    
    def removeNodeAt(self,index):
        
        if index == 0:
            self.removeHead()
        
        elif index < 0:
            raise Exception("Please insert valid index")
        elif index == self.size-1:
            self.removeTail()
            
        else:
            temp1 = self.head
            temp2 = self.head
        
            i = 0
            j = 0
            while(i!=index):
                temp1 = temp1.next
                i+=1
            
            while(j!= index-1):
                temp2 = temp2.next
                j+=1
                    
            temp2.next = temp1.next
            temp1 = None
        self.size -= 1


    def addLast(self, data):
        
        if self.size == 0:
            node = Node(data)
            self.head = node
            self.tail = node
        else:
            node = Node(data)
            self.tail.next = node
            self.tail = self.tail.next
        self.size+=1
    
    def tailitem(self):
        return self.tail.data    
    
    def headitem(self):
        return self.head.data
    
    def removeHead(self):
        if self.size == 0:
            IndexError("LinkedList is empty!")
        else:
            self.head = self.head.next
            self.size -= 1
        
    def removeTail(self):
        if self.size == 0:
            raise IndexError("LinkedList is empty!")
        else:
            x = self.head
            i = 0
            while(i != self.size-2):
                x = x.next
                i+=1
            
            self.tail = x
            x.next = None
            
        self.size -= 1