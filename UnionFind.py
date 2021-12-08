class Node:
    def __init__(self,data=None,parent=None):
        self.data = data
        self.parent = parent
    
class UnionFind:
    def __init__(self):
        self.table = []
        self.group = []
    
    def printTable(self):
        for node in self.table:
            print(node.data, end=" ")
        print("\n")
    
    def printGroup(self):
        for vals in self.group:
            print(vals)

    def add(self,data):
        self.table.append(Node(data))
    
    def add_list(self,arr):
        for i in arr:
            self.table.append(Node(i))
    
    def union(self,data1,data2):
        node1 = Node(data1)
        node2 = Node(data2)
        
        if node1.parent == None and node2.parent == None:
            node2.parent == node1
            
        else:
            temp1 = node1.parent
            temp2 = node2.parent
            while temp1 != None:
                temp1 = temp1.parent
            while temp2 != None:
                temp2 = temp2.parent
            temp2.parent = temp1
    
        self.updateTable()
        return
    

    def updateTable(self):
        for i in range(len(self.table)):
            temp = self.table[i]
            temp_res = []
            if temp.parent != None:
                temp_res.append(temp.data)
                while temp.parent != None:
                    temp = temp.parent
                    temp_res.append(temp.data)
                self.group.append(temp_res)
    
    def findGroup(self,data):
        for i in self.group:
            for j in i:
                if j == data:
                    return i
        return -1
