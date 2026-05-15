import pandas as pd

# Load dataset
orders = pd.read_csv("C:/Users/jagru/OneDrive/文件/AI-Powered E-Commerce sales and Customer intelligence syatem/datasets/olist_orders_dataset.csv")

# Display first 5 rows
print("FIRST 5 ROWS:")
print(orders.head())

# Total rows and columns
print("\nDATASET SHAPE:")
print(orders.shape)
# Check missing values
print("\nMISSING VALUES:")
print(orders.isnull().sum())
# Order status analysis
print("\nORDER STATUS COUNTS:")
print(orders["order_status"].value_counts())
# Convert purchase timestamp to datetime
orders["order_purchase_timestamp"] = pd.to_datetime(
    orders["order_purchase_timestamp"]
)

# Extract month name
orders["order_month"] = orders["order_purchase_timestamp"].dt.month_name()

# Monthly order trend
print("\nMONTHLY ORDER TREND:")
print(orders["order_month"].value_counts())
import matplotlib.pyplot as plt

# Monthly trend chart
monthly_orders = orders["order_month"].value_counts()

monthly_orders.plot(kind="bar")

plt.title("Monthly Order Trend")
plt.xlabel("Month")
plt.ylabel("Total Orders")

plt.show()