"""Use sns.countplot() to visualize the number of orders placed by each payment method 
(e.g., UPI, Card, Cash) in a sample Swiggy orders DataFrame with at least 3 payment types.
"""

import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

swiggy_orders = pd.DataFrame({
    'Order_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Payment_Method': ['UPI', 'Card', 'Cash', 'UPI', 'Card', 'Cash', 'UPI', 'Card', 'Cash', 'UPI']})

sns.countplot(x="Payment_Method", data=swiggy_orders)
plt.title("Number of orders by Payment method")
plt.xlabel("Payment Method")
plt.ylabel("Number of Orders")
plt.show()

