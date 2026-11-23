"""Use the pairplot function to visualize the 'tips' dataset,
 but this time set the hue parameter to 'sex' and observe how the data points are colored based on gender.
"""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the 'tips' dataset from seaborn
tips = sns.load_dataset('tips')

# Create a pairplot with hue set to 'sex'
sns.pairplot(tips, hue="sex", palette="Set2")
plt.show()