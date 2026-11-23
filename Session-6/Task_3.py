"""visualize how the number of likes and comments are related in a dataset of Instagram posts."""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# read CSV file and load data

df = pd.read_csv("D:/Data Analytics/DA-Visualization-with-Seaborn/Session-6/instagram_posts.csv")

# visualize how the number of likes and comments are related in a dataset of Instagram posts.

g = sns.jointplot(data=df, x="likes", y="comments", kind='kde', height=6)

g.set_axis_labels("Number of Likes", "Numbers of Comments")
g.figure.suptitle("Likes vs comments on instagram posts", y=1.02)

plt.show()