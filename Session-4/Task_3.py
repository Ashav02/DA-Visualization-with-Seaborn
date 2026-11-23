"""Given an array of IPL match ticket prices, plot a boxplot using sns.boxplot() and identify any outliers in the data.
<br><br><em><strong>Hint:</strong> Outliers are points that appear outside the whiskers of the boxplot.</em>
"""

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# Sample array of IPL match ticket prices
ticket_prices = np.random.randint(100, 1000, size=100)


# Create a boxplot using seaborn
sns.boxplot(x=ticket_prices, notch=True, whis=1.5)

plt.title("Boxplot of IPL Match Ticket Prices")
plt.xlabel("Ticket Prices")
plt.ylabel("Frequency")

plt.show()