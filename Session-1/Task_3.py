"""Recreate the above line plot using Seaborn's axes-level and figure-level functions separately. 
Briefly note one difference you observe in how these functions work.
<br><br><em><strong>Hint:</strong> Use sns.lineplot() for axes-level and sns.relplot() for figure-level.</em>
"""

import pandas as pd
import seaborn as sns   
import matplotlib.pyplot as plt

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
temps = [32, 34, 33, 35, 36, 37, 34]

# Create a DataFrame for the data
data = pd.DataFrame({'Days': days, 'Temperature': temps})

# Axes-level function using sns.lineplot()
plt.figure(figsize=(10, 6))
sns.lineplot(data=data, x='Days', y='Temperature', marker='o', color='b')
plt.xlabel('Days')
plt.ylabel('Temperature (°F)')
plt.grid(alpha=0.3)
plt.show()
