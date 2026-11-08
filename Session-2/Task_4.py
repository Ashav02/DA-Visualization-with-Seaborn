"""Plot a countplot of movie genres from a BookMyShow-style dataset,
but remove the confidence interval from the plot.
<br><br><em><strong>Hint:</strong> Use the ci=None parameter to remove confidence intervals in sns.barplot().</em>
"""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

movie_data = pd.DataFrame({
    'Movie_Genre': ['Action', 'Comedy', 'Drama', 'Horror', 'Action', 'Comedy', 'Drama', 'Horror', 'Action', 'Comedy'],
    'Ticket_Sales': [100, 150, 200, 80, 120, 180, 220, 90, 130, 160]})

sns.barplot(x="Movie_Genre", y="Ticket_Sales", data=movie_data, ci=None, hue="Movie_Genre")
plt.title("Ticket Sales by Movie Genre")
plt.xlabel("Movie Genre")
plt.ylabel("Ticket Sales")
plt.show()
