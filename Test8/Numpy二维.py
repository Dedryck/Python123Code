import numpy
arr = numpy.array([[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10]])

arr.dtype = 'int64'
print("创建的数组为：")
print(f"{arr}")
print(f"创建的数组维度为：{arr.shape}")
print(f"数组类型为：{arr.dtype}")
print(f"数组元素个数为：{arr.size}")
print(f"数组每个元素大小为：{arr.itemsize}")