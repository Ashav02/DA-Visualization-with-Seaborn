"""Import Seaborn and use sns.histplot() to visualize the distribution of delivery times (in minutes)
 from a sample Swiggy order dataset with at least 30 values.
"""


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd 

swiggy_order_data = pd.DataFrame({'Delivery_time': [30, 25, 40, 35, 20, 47, 50, 30, 28, 39, 33, 21, 45, 44, 37,
                                                    51, 33, 27, 42, 34, 23, 41, 54, 36, 25, 40, 35, 20, 47, 49]})

sns.histplot(data=swiggy_order_data, x="Delivery_time", bins=10, kde=True)
plt.xlabel("Delivery Time (min)")
plt.ylabel("Frequency")
plt.title("Distribution of Delivery Times for Swiggy Orders")
plt.show()