class Hashtable:
    def __init__(self, length=8, loadFactor = 0.6):
        self.length = length
        self.loadFactor = loadFactor
        self.table = [None]*self.length
    

    #Print The Whole table function
    def printht(self):
        print(self.table)
    
    #Function to get the index of the (key,value) pair in the hash table
    def hash_func(self, key):
        datatypes = [str,int]

        if type(key) in datatypes:
            if type(key) == str:
                indx = 0

                for i in key:
                    ascii_num = ord(i)
                    indx+=(ascii_num%22)

                return (indx%self.length)
            else:
                return (key%self.length)

    #In case of Hash collision we need to use the Double Hashing to get the new index 
    def double_hashing(self,key):
        datatypes = [str,int]

        if type(key) in datatypes:
            if type(key) == str:
                indx = 0

                for i in key:
                    ascii_num = ord(i)
                    indx+=(ascii_num%23)

                return(indx%10)
            else:
                return(key%self.length)


    #function to get the size of the array in case of Open Addressing
    def checkSize(self):
        x =0

        temp_arr = []
        
        for i in self.table:
        
            if i != None:
                x+=1
                temp_arr.append(i)
        
        if x > self.loadFactor*self.length:
        
            self.length = self.length*2
            self.table = [None]*self.length
        
        
            for i in temp_arr:
                self.add(i[0],i[1])

    #function to add element in the hash table
    def add(self,key,value):
        index = self.hash_func(key)
        
        if self.table[index] == None or self.table[index] == "Tombstone":
            self.table[index] = (key,value)
        
        else:
            x = 0
            
            if self.double_hashing(key) == 0:
                x=1
            
            while self.table[index] != None :
                index = (index + x*(self.double_hashing(key)))%self.length
                x = x+1
            self.table[index] = (key,value)
        
        self.checkSize()


    def remove(self,key):
        index = self.hash_func(key)
        temp = self.table[index]

        if temp[0] == key:
            self.table[index] = "Tombstone"
        
        elif temp[0] != key or temp == "Tombstone":
            x = 0

            if self.double_hashing(key) == 0:
                x = 1
            
            while self.table[index][0] != key:
                index = (index + x*(self.double_hashing(key)))%self.length
                x +=1
            self.table[index] = "Tombstone"


    def getValue(self,key):
        index = self.hash_func(key)
        temp = self.table[index]

        if temp != "Tombstone" or temp != None :
            if temp[0] ==key:
                return temp[1]
            else:
                x = 0

            if self.double_hashing(key) ==0:
                x = 1
            while self.table[index][0] != key:
                index = (index+x*(self.double_hashing(key)))%self.length
                x+=1
            return self.table[index][1]
        
        elif temp == None:
            return None


        else:
            x = 0

            if self.double_hashing(key) ==0:
                x = 1
            while self.table[index] != "Tombstone":
                index = (index+x*(self.double_hashing(key)))%self.length
                x+=1
            return self.table[index][1]

ht = Hashtable()
ht.add(5,12)
ht.add(44,1)
ht.add(21,4)
ht.add(35,6)
ht.add(0,4)
ht.add(3,9)
ht.printht()
print(ht.getValue(3))