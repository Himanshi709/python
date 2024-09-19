import numpy as np

#creating array using numpy
arr=np.array([1,2,3,4,5])
arr2=np.array([1,2,5,7,435,23,687,433,7,90,45])
print(arr)

#print the type of array
print(type(arr))
print(arr.max())
print(arr.min())
print(arr.mean())
arr2.sort()
print(arr2)
a=np.flip(arr2)
print(a)
