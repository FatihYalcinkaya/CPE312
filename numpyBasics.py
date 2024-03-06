import numpy as np

array=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print("vector:",array)
a=array.reshape(3,5)
print("two dimensional array ",a)

print("shape",a.shape)
print("dimesion:",a.ndim)
print("data type",a.dtype.name)
print("size",a.size)
print("type",type(a))

x=np.array([1,2,3])
y=np.array([4,5,6])
print(x+y)
print(x-y)
print(x**2)

a=np.array([1,2,3,4,5,6,7])
print(a[0])
print(a[0:4])

reverse_array=a[::-1]
print(reverse_array)
