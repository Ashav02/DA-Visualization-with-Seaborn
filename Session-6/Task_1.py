"""Load a CSV file containing Flipkart product ratings and prices, then use Seaborn's jointplot with kind='scatter' 
to visualize the relationship between rating and price.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# load data

df = pd.read_csv("D:/Data Analytics/DA-Visualization-with-Seaborn/Session-6/flipkart_products.csv")

# clean Price : remove ₹ and commas, then convert to number
df["Price"] = (df["Price"].astype(str).str.replace("[₹,]", "", regex=True).astype(float))

# drop rows with missing value
df = df.dropna(subset=["Rating", "Price"])



# visualize the relationship between rating and price.
g= sns.jointplot(data=df, x='Rating', y='Price' ,kind="scatter", height=6, alpha=0.5)

g.set_axis_labels("Rating", "Price")
g.figure.suptitle("Relationship between rating and price", y=1.02)

plt.show()
