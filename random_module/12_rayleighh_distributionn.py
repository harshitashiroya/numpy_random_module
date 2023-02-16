#RAYLEIGH DISTRIBUTION

"""
Rayleigh distribution is used in signal processing.

It has two parameters:
scale - (standard deviation) decides how flat the distribution will be default 1.0).
size - The shape of the returned array.

"""

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.rayleigh(scale=3, size=(2, 3))
print(x)

#visualization

sns.distplot(random.rayleigh(size=50), hist=False)

plt.show()


