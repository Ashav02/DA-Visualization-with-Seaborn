"""Modify your barplot to display the total number of orders instead of the average
 by setting estimator to sum in sns.barplot().
"""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

zomato_data = pd.DataFrame({
    'Food_Category': ['Pizza', 'Burger', 'Biryani', 'South Indian', 'Pizza', 'Burger', 'Biryani', 'South Indian', 'Pizza', 'Burger'],
    'Delivery_Time_mins': [30, 25, 40, 35, 28, 22, 38, 33, 32, 27]})

sns.barplot(x="Food_Category", y="Delivery_Time_mins", hue="Food_Category" ,data=zomato_data, estimator=sum)
plt.title("Total Delivery Time by Food Category")
plt.xlabel("Food Category")
plt.ylabel("Total Delivery Time (mins)")
plt.show()

