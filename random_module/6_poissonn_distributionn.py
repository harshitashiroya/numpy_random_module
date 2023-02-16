# POISON DISTRIBUTION

"""
Poisson Distribution is a Discrete Distribution.
It estimates how many times an event can happen
in a specified time.

It has two parameters:

lam - rate or known number of occurences.
size - The shape of the returned array.
"""

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.poisson(lam=2,size=5)
print(x)

#visualization

sns.distplot(x)
# or... sns.distplot(random.poisson(lam=2, size=1000), kde=False)
plt.show()

"""
Difference Between Poisson and Binomial Distribution

The difference is very subtle it is that, 
binomial distribution is for discrete trials, 
whereas poisson distribution is for continuous trials.

But for very large n and near-zero p binomial distribution is 
near identical to poisson distribution such that 
n * p is nearly equal to lam.
"""