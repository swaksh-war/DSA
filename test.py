<<<<<<< HEAD
=======
from dynamic_arr1 import DynamicArray

arr = DynamicArray(['sun', 'mon'])
arr.append('tues')
print(arr)
arr.insertAt('wed',1)
print(arr)
print(len(arr))
arr.pop(0)
print(arr)
print(len(arr))
arr.pop()
print(arr)
print(len(arr))

a = DynamicArray([1,2,3])
b = [4,5,6]
a.extend(b)
print(a)
a.clear()
print(a)
>>>>>>> fae9b31e996b9b3d444a7b7efc46cf8d752e7b29
