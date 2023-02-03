# Question 1
print("\n Q1")
list_1 = [-1, 2, 3, 9, 0]
list_2 = [1, 2, 7, 10, 14]
print(list_1 + list_2)

# Question 2
print("\n Q2")
list_1 = [-1, 2, 3, 9, 0]
list_2 = [1, 2, 7, 10, 14]

for i in range(0, len(list_1)):
    list_1[i] = list_1[i] + list_2[i]

print (list_1)

# Question 3 
import numpy as np
print("\n Q3")
a = np.arange(12).reshape(2,3,2,1)
print(a.shape)

# Question 4
arr = np.arange(27).reshape(3,3,3)
print("\n Q4")
print("\nTest1")
print (arr[:,:,0])
print("\nTest2")
print (arr[1,1,:])
print("\nTest3")
print (arr[:, 0:3:2, 0:3:2])

# Question 5
arr = np.arange(27).reshape(3,3,3)
print("\n Q5")
print("\nTest1")
print (arr[0,1,1])
print (arr[1,2,2])
print (arr[2,0,0])

print("\nTest2")
print (arr[1,0,0])
print (arr[1,2,2])

# Question 6
print("\n Q6")
a = np.arange(-10,20).reshape(5,6)
sum_cols = a.sum(axis=0)
for i in range(0, len(sum_cols)):
    if (sum_cols[i] % 10 == 0):
        print(a[:,i])