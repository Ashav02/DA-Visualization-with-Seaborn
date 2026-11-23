"""Use sns.violinplot() to compare the order amounts for two different Zomato restaurant categories
 (e.g., 'Fast Food' vs 'Desserts') from a sample dataset.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("zomato_sample_data.csv")

# Filter the dataset for the two restaurant categories
categories = ['Fast Food', 'Desserts']
filtered_data = data[data['Category'].isin(categories)]

# Create the violin plot
plt.figure(figsize=(10, 6))
sns.violinplot(data=filtered_data, x='Category', y='Order Amount')
plt.title('Comparison of Order Amounts by Restaurant Category')
plt.xlabel('Restaurant Category')
plt.ylabel('Order Amount')
plt.show()