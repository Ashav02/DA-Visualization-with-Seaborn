"""Create a violin plot using sns.violinplot() to show the distribution of daily step counts collected from a fitness app like Google Fit,
   and explain what the shape of the plot tells you about user activity.
"""

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Sample array of daily step counts
daily_steps = np.random.randint(1000, 20000, size=100)

# Create a violin plot using seaborn
sns.violinplot(data=daily_steps, inner="quartile", color="lightblue")

plt.title("Violin Plot of Daily Step Counts")
plt.xlabel("Daily Step Counts")
plt.ylabel("Density")

plt.show()