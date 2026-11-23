"""Create a jointplot with kind='hex' to analyze the relationship between delivery time and order value using a dataset of Swiggy food orders.
<br><br><em><strong>Hint:</strong> Use sns.jointplot(x='delivery_time', y='order_value', data=your_dataframe, kind='hex').</em>
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load csv file

df = pd.read_csv("D:/Data Analytics/DA-Visualization-with-Seaborn/Session-6/swiggy_food_orders.csv")

# Drop rows with missing values
df = df.dropna(subset=["Delivery_Time_Min", "Total_Amount"])

#  the relationship between delivery time and order value

g = sns.jointplot(data=df, x="Delivery_Time_Min", y="Total_Amount", kind="hex", height=6)

g.set_axis_labels("Delivery Time", "Order Value")
g.figure.suptitle("Delivery Time vs Order Value", y=1.02)

plt.show()
