import time

def timer(x):
    first = time.time()
    x()
    last = time.time()
    print(last-first) 
