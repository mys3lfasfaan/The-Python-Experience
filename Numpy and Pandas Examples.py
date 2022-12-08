import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))
print(np.__version__)

a1=np.array([1,2,3])

a2=np.array([[1,2,3.3],[4,5,6.5]])

a3=np.array([[[1,2,3],
[4,5,6],
[7,8,9]],
[[10,11,12],
[13,14,15],
[16,17,18]]])

print("Shape details: ")
print(a1.shape)
print(a2.shape)
print(a3.shape)
print("")

print("Dimensions: ")
print(a1.ndim,a2.ndim,a3.ndim)
print("")

print("Type of array:")
print(a1.dtype,a2.dtype,a3.dtype)
print("")

print("Size:")
print(a1.size,a2.size,a3.size)
print("")

print("Type of variable:")
print("")
print(type(a1),type(a2),type(a3))
print("")
print("")

import pandas as pd
df1=pd.DataFrame(a1)
df2=pd.DataFrame(a2)
print(df1)
print(df2)

arr = np.array([1,2,3])

ones = np.ones((2,3))
print(ones)
print("\n")

zeros = np.zeros((2,3))
print(zeros)
print("\n")

r = np.arange(0,10,2)
print(r)
