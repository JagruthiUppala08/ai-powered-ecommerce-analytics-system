import pandas as pd

# Load dataset
df = pd.read_csv(r"C:\Users\jagru\OneDrive\文件\AI-Powered E-Commerce sales and Customer intelligence syatem\datasets\olist_order_payments_dataset.csv")

# Show first 5 rows
print(df.head())
print("Total Revenue:")
print(df["payment_value"].sum())
print("Average Payment Value:")
print(df["payment_value"].mean())
print("\nPayment Method Distribution:\n")

print(df["payment_type"].value_counts())

import matplotlib.pyplot as plt

payment_counts = df["payment_type"].value_counts()

payment_counts.plot(kind="bar")

plt.title("Payment Method Distribution")
plt.xlabel("Payment Type")
plt.ylabel("Count")

plt.show()

# IF YOU WANT IN PIE CHART, UNCOMMENT BELOW CODE

#payment_counts.plot(kind="pie", autopct="%1.1f%%")

#plt.title("Payment Method Distribution")

#plt.ylabel("")

#plt.show()