from stack import Stack
from timer import timer

s = Stack([1,2,3,4])
def print_():
    print(s)
    
timer(print_)

from Queue import queue

q = queue([1,2,3,4])
q.enqueue("a")
print(q.head())
print(q.tail())
print(q) 
