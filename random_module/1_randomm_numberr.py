from numpy import random

# generate random integer in specific range

i = random.randint(200) # 0 t0 200
print(i)

# flat between 0 t0 1

fl = random.rand()
print(fl)

# random array - size parameter

arr = random.randint(200, size=(6))  # array contains 6 random integer from 0 to 200
print(arr)


# 2D array

print("\n")
arr_2d = random.randint(200,size=(3,4)) # 3 row each contains 4 elements
print(arr_2d)

# 1D array containing 5 random floats
print("\n")
arr_1d = random.rand(5)
print(arr_1d)

arr_2d_fl = random.rand(3,5) # 2d array, 3 row, 5 float elements
print(arr_2d_fl)
print("\n")

# random number from array
ch = random.choice([1,78,90,35,67])
print(ch)
print("\n")

# The choice() method also allows you to return an array of values.

ar_val = random.choice([12,32,21,3,4],size=(3,5))
print(ar_val)
print("\n")

print("Data Distribution")
"""
DATA DISTRIBUTION

Data Distribution is a list of all possible values, 
and how often each value occurs.

The random module offer methods that returns 
randomly generated data distributions.

We can generate random numbers based on defined probabilities 
using the choice() method of the random module.

The choice() method allows us to specify the probability for each value.

The probability is set by a number between 0 and 1, 
where 0 means that the value will never occur 
and 1 means that the value will always occur.

The sum of all probability numbers should be 1.
"""

data_dis = random.choice([3, 9, 7, 89], p=[0.1, 0.3, 0.6, 0.0], size=(100))
print(data_dis)

# 2D array

data_dis_2d = random.choice([23,56,78,90], p=[0.2,0.3,0.4,0.1], size=(3,4))
print(data_dis_2d)