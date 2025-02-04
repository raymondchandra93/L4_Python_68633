import numpy as np

# -- Numpy Array
mylist = [1, 2, 3, 4, 5]
# print(mylist)

myarray = np.array(mylist) 
#print(myarray)

# print(mylist * 2)
# print(myarray * 2)

# -- Numpy Reshape
myarray = np.array([1, 2, 3, 4, 5, 6]) 

reshaped_arr = myarray.reshape(3, 2)        # reshaping the array into 2 rows & 3 columns
#print(reshaped_arr)

# -- Numpy Arrange
arranged_arr = np.arange(3)                 # [0, 1, 2] - return element start 0, stop before 3, step 1
#print(arranged_arr)

arranged_arr = np.arange(3, 7, 2)           # [3, 5] - return element start 3, stop before 7, step 2
#print(arranged_arr)

# -- Numpy Zeros
zeros_arr = np.zeros((2, 3))                # 2 rows, 3 cols of zero arrays
# print(zeros_arr)

# -- Numpy Ones
ones_arr = np.ones((2, 3))                   # 2 rows, 3 cols of ones arrays
# print(ones_arr)

# -- Numpy Linspace
linspace_arr = np.linspace(0, 11, 5)        # generate 5 evenly spaced numbers from 0 - 10
# print(linspace_arr)

# -- Numpy Statistical Functions
stat_arr = np.array([10, 20, 30, 40, 50])

# print(np.median(stat_arr))
# print(np.mean(stat_arr))
#print(np.std(stat_arr))
#print(np.min(stat_arr))
#print(np.max(stat_arr))

# -- Numpy Indexing and Slicing
id_arr = np.array([10, 20, 30, 40, 50])

print(id_arr[0])
print(id_arr[-1])
print(id_arr[1:4])