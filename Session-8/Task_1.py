"""Using Seaborn's lineplot(), plot the daily temperature trend for one week using the following data: days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
 temps = [32, 34, 33, 35, 36, 37, 34]. Label the axes and title the chart 'Weekly Temperature Trend'.
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
temps = [32, 34, 33, 35, 36, 37, 34]

# Create a DataFrame for the data
data = pd.DataFrame({'Days': days, 'Temperature': temps})

# Plot the lineplot
sns.lineplot(data=data, x='Days', y='Temperature', marker='o', color='b')
plt.xlabel('Days')
plt.ylabel('Temperature (°F)')
plt.title('Weekly Temperature Trend')
plt.tight_layout()
plt.grid(alpha=0.3)
plt.show()