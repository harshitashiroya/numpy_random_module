# MULTINOMIAL DISTRIBUTION

"""
Multinomial Distribution

Multinomial distribution is a generalization of binomial distribution.

It describes outcomes of multi-nomial scenarios
unlike binomial where scenarios must be only one of two.
e.g. Blood type of a population, dice roll outcome.

It has three parameters:
n - number of possible outcomes
pvals - list of probabilties of outcomes.
size - The shape of the returned array.
"""

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.multinomial(n = 4, pvals=[1/4,1/4,1/4,1/4])
print(x)

sns.histplot(x)
plt.show()