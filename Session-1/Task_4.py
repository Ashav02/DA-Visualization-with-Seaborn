"""Apply each of Seaborn's built-in themes (darkgrid, whitegrid, ticks) to your temperature trend plot and save three separate images.
Compare how the grid and background change with each theme.
<br><br><em><strong>Hint:</strong> Use sns.set_theme(style='theme_name') before plotting.</em>
"""

import seaborn as sns
import matplotlib.pyplot as plt

days = list(range(1,11))
temp = [28, 30, 31, 29, 33, 35, 34, 32, 31, 30]

themes = ["darkgrid","withegrid","ticks"]

for theme in themes:
    sns.set_theme(style=theme)         
    plt.figure(figsize=(8, 4))          
    sns.lineplot(x=days, y=temp, marker="o")
    plt.title(f"Temperature Trend - {theme}")
    plt.xlabel("Day")
    plt.ylabel("Temperature (°C)")
    plt.savefig(f"temperature_{theme}.png", dpi=150)   
    plt.show()

