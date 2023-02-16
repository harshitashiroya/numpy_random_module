#CHI SQUARE DISTRIBUTION

"""
Chi Square distribution is used as a basis to verify the hypothesis.

It has two parameters:
df - (degree of freedom).
size - The shape of the returned array.
"""

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.chisquare(df=2, size=(3,3))
print(x)

#visualization

sns.displot(x)
plt.show()