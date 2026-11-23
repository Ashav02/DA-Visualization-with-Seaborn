"""Compare the visual insights you get from scatter, hexbin, and KDE jointplots using the same dataset of Zomato restaurant reviews (rating vs number of reviews). Briefly describe which plot type helps you understand the data best and why.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# read data 
df = pd.read_csv("D:/Data Analytics/DA-Visualization-with-Seaborn/Session-6/zomato_rating_vs_reviews.csv")


# review are skewed, so use log scale
df["log_review"] = np.log10(df["number_of_reviews"])

# Compare the visual insights you get from scatter, hexbin, and KDE
for kind in ["scatter", "hex", "kde"]:
    g = sns.jointplot(data=df, x="rating", y="log_reviews", kind=kind, height=5)
    g.set_axis_labels("Raating", "log10(Number of reviews)")
    g.figure.suptitle(f"{kind.upper()} joinplot", y=1.02)

plt.show()