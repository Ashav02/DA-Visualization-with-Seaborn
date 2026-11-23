"""Given a dataset of IPL match scores, use sns.histplot() to plot the run distribution. 
Change the number of bins and observe how the plot changes. Write 2-3 lines about what you notice.
<br><br><em><strong>Hint:</strong> Try bins=5, bins=10, and bins=20.</em>
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ipl_data = pd.DataFrame({'Runs': [50, 75, 120, 90, 150, 80, 110, 130, 70, 95, 140, 100, 60, 125, 115, 85, 105, 95, 130, 120]})

sns.histplot(data=ipl_data,
             x="Runs",
             bins=10,
             color='lightgreen',
             alpha=0.5)

plt.xlabel("Runs")
plt.ylabel("Frequency")
plt.title("Distribution of IPL Match Scores")

plt.show()