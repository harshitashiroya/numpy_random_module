#UNIFORM DISTRIBUTION

"""
Used to describe probability where every event has equal chances of occuring.
E.g. Generation of random numbers.

It has three parameters:
a - lower bound - default 0 .0.
b - upper bound - default 1.0.
size - The shape of the returned array.
"""


from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.uniform(low=0,high=10,size=(2,3))
# fill the array with 0 to 10 value but not repeated
print(x)

#visualization

# sns.distplot(x)
sns.distplot(random.uniform(low=10,high=100,size=(3,3)))
plt.show()