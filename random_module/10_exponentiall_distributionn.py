#EXPONENTIAL DISTRIBUTION

"""
Exponential Distribution

Exponential distribution is used for describing time
till next event e.g. failure/success etc.

It has two parameters:
scale - inverse of rate ( see lam in poisson distribution ) defaults to 1.0.
size - The shape of the returned array.
"""

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns


x = random.exponential(scale=2,size=(3,3))
print(x)

#visualization

sns.histplot(x)
plt.show()

"""
Relation Between Poisson and Exponential Distribution

Poisson distribution deals with number of occurences of an event 
in a time period 
whereas 
exponential distribution deals with 
the time between these events.
"""