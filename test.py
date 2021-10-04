from linked_list import LinkedList

m = LinkedList()
m.addBegin(1)
m.addLast(2)
m.addLast(3)
m.addLast(4)
m.addLast(5)
# m.removeHead()
# m.addAfter(7,0)
print(m)
m.removeTail()
print(m)

print(m.tailitem())