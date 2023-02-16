
"""
Visualize Distributions With Seaborn
Seaborn is a library that uses Matplotlib underneath to plot graphs.
It will be used to visualize random distributions.

pip install seaborn


Distplots
Distplot stands for distribution plot,
it takes as input an array and plots a curve corresponding
to the distribution of points in the array.

Import Matplotlib
import matplotlib.pyplot as plt
"""


# plotting a Distplot

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

ar = np.array([1,3,2,4,5])
sns.distplot(ar, hist=False)
#sns.distplot(ar)
plt.show()