"""Download or create a list of daily step counts (e.g., from a fitness app)
 for one month and plot the distribution using sns.kdeplot(), showing the probability density curve.
"""

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

steps = np.random.randint(3000, 15000, size=30)

sns.kdeplot(steps, shade=True, color='blue', alpha=0.5)
plt.title('Distribution of Daily Step Counts')
plt.xlabel('Daily Step Counts')
plt.ylabel('Density')
plt.show()