"""Create a pairplot for the 'tips' dataset with the hue set to 'smoker',
 and set the diag_kind parameter to 'kde' to show kernel density estimates on the diagonal plots.
 <br><br><em><strong>Hint:</strong> Use diag_kind='kde' in the pairplot function.</em>
"""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


# Load the 'tips' dataset from seaborn
tips = sns.load_dataset('tips')

# Create a pairplot with hue set to 'smoker' and diag_kind set to 'kde'
sns.pairplot(tips, hue="smoker", diag_kind='kde', palette="Set2")

plt.show()