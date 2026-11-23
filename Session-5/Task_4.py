"""Pick any two numerical columns from the 'tips' dataset and use pairplot to visualize only those columns,
setting hue to 'time' (Lunch/Dinner).<br><br><em><strong>Constraint:</strong> Use the vars parameter to select the columns.</em>
"""

import seaborn as sns 
import matplotlib.pyplot as plt
import pandas as pd

# Load the 'tips' dataset from seaborn
tips = sns.load_dataset('tips')

# Create a pairplot for two numerical columns with hue set to 'time'
sns.pairplot(tips, vars=["total_bill", "tip"], hue="time")

plt.show()