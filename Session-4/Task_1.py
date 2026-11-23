"""Load a CSV file containing Flipkart product prices and use sns.boxplot() to visualize the price distribution.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("flipkart_products.csv")

sns.boxplot(data=df,
            x="Price",
            color="Red",
            width=0.5)

plt.xlabel("Price (₹)")
plt.title("Price Distribution of Flipkart Products")

plt.show()
    