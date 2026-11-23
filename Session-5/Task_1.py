"""Load the 'tips' dataset from seaborn and create a basic pairplot for all numerical columns.
"""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the 'tips' dataset from seaborn
tips = sns.load_dataset('tips')

# Create a basic pairplot for all numerical columns
sns.pairplot(tips, palette="Set2")

plt.show()