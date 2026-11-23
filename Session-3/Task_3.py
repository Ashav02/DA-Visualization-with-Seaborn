"""Combine sns.histplot() and sns.kdeplot() to visualize the distribution of monthly spending amounts (in rupees) on Zomato orders,
 using the same dataset for both plots on a single figure.
 <br><br><em><strong>Hint:</strong> Use the same data and overlay the KDE curve on the histogram by calling both functions on the same axes.</em>
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

order_data = pd.DataFrame({'Monthly_Spending': [500, 750, 1200, 900, 1500, 800, 1100, 1300, 700, 950,
                                                1400, 1000, 600, 1250, 1150, 850, 1050, 950, 1300, 1200,
                                                700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600]})

plt.figure(figsize=(10, 6))

sns.histplot(data=order_data,
             x="Monthly_Spending", 
             bins=8, 
             kde=False,
             color='lightblue', 
             alpha=0.5)

sns.kdeplot(data=order_data,
            x="Monthly_Spending", 
            color='red', 
            linewidth=2)

plt.xlabel("Monthly Spending (₹)")
plt.ylabel("Frequency / Density")
plt.title("Distribution of Monthly Spending on Zomato Orders")
plt.legend(['KDE Curve', 'Histogram'])

plt.show()