import numpy as np

python_list = [1,2,3,4,5,6]


two_dimensional_list = [[0,1,2], [3,4,5]]

nparray = np.array(python_list, dtype=int)

print(nparray)
print(nparray + 10)
print(nparray / 10)
print(nparray * 3)


numpy_bool_array = np.array([0, 1, -1, 0, 0], dtype=bool)
print(numpy_bool_array)

two = np.array(two_dimensional_list)

lst = nparray.tolist()

print(lst)

print(two.shape)
print(two.size)
print(nparray.size)




print(two[::-1,::-1])
print(two.reshape(3,2).flatten())
print(np.hstack((nparray, two.flatten())))
print(np.vstack((nparray, two.flatten())))

rnd = np.random.randint(6, size=(3,2))

print(rnd)