class Node:
    def __init__(self,data, next = None):
        self.data = data
        self.next = next
    
    def getData(self):
        return self.data
    
    def setData(self, data):
        self.data = data
    
    def getNextNode(self):
        return self.next
    
    def setNextNode(self, node):
        self.next = node

class LinkedList:
    def __init__(self, head = None):
        self.head = head
        self.size = 0
    
    def getSize(self):
        return self.size
    
    def addNode(self, data):
        node = Node(data, self.head)
        self.head = node
        self.size+=1
        return True
    
    def removeNode(self, value):
        prev = None
        curr = self.head
        while curr:
            if curr.getData() == value:
                if prev:
                    prev.setNextNode(curr.getNextNode())
                else:
                    self.head = curr.getNextNode()
                return True
            prev = curr
            curr = curr.getNextNode()
        return False
    
    def findNode(self, value):
        curr = self.head
        while curr:
            if curr.getData() == value:
                return True
            else:
                curr = curr.getNextNode()
        return False
    
    def insertNodeatEnd(self,data):
        node = Node(data)
        if self.head == None:
            self.head = node
        last = self.head
        while(last.next):
            last = last.next
        last.next = node
    
    def insertInBetween(self, data, node_num):
        if node_num == None:
            print ("index not found")
        node = Node(data)
        node.next = node_num.next
        node_num.next = node
    
    def printLinkedList(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.getNextNode()

m = LinkedList()
m.addNode(1)
m.addNode(2)
m.addNode(3)
m.insertNodeatEnd(5)
m.insertNodeatEnd(7)
m.printLinkedList()