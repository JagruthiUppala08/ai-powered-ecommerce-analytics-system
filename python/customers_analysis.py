import pandas as pd

# Load dataset
df = pd.read_csv(r"C:\Users\jagru\OneDrive\文件\AI-Powered E-Commerce sales and Customer intelligence syatem\datasets\olist_customers_dataset.csv")

# Show first 5 rows
print(df.head())

print("Total Customers:")
print(df["customer_id"].count())

print("\nCustomers by State:\n")

print(df["customer_state"].value_counts())

import matplotlib.pyplot as plt

state_counts = df["customer_state"].value_counts()

state_counts.plot(kind="bar")

plt.title("Customer Distribution by State")
plt.xlabel("State")
plt.ylabel("Customers")

plt.show()