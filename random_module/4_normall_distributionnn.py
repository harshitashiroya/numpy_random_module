#Normal Distribution

"""
also known as GAUSSIAN Distribution

use random.normal() method

3 parameters:
1. loc - (MEAN) where the peak of the bell exists
2. scale - (STANDARD DEVIATION) how flat the graph distribution should be.
3. size - The shape of the returned array.
"""
"""
Mean is nothing but the average of the given set of values. 
It denotes the equal distribution of values for a given data set.


"""
#Generate a random normal distribution of size 2x3:

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.normal(size=(2,4))
print(x)

#Generate a random normal distribution of size 2x3 with mean at 1 and standard deviation of 2:
print("\n")
y = random.normal(loc=1, scale = 2, size=(2,4))
print(y)
print("\n")

#visualization

sns.histplot(random.normal(loc=1, scale=2, size=(2,5)))
plt.show()