"""Create a barplot using sns.barplot() to show the average delivery time (in minutes)
 for each food category (e.g., Pizza, Burger, Biryani, South Indian) from a Zomato-style dataset.
 <br><br><em><strong>Hint:</strong> Use the estimator parameter to show the mean delivery time for each category.</em>
"""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

zomato_data = pd.DataFrame({
    'Food_Category': ['Pizza', 'Burger', 'Biryani', 'South Indian', 'Pizza', 'Burger', 'Biryani', 'South Indian', 'Pizza', 'Burger'],
    'Delivery_Time_mins': [30, 25, 40, 35, 28, 22, 38, 33, 32, 27]})

sns.barplot(x='Food_Category', y='Delivery_Time_mins', data=zomato_data, estimator=lambda x: sum(x)/len(x))
plt.title("Average Delivery Time by Food Category")
plt.xlabel("Food Category")
plt.ylabel("Average Delivery Time (mins)")
plt.show()