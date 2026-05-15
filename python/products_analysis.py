import pandas as pd

# Load dataset
df = pd.read_csv(r"C:\Users\jagru\OneDrive\文件\AI-Powered E-Commerce sales and Customer intelligence syatem\datasets\olist_products_dataset.csv")

# Show first 5 rows
print(df.head())

print("Total Products:")
print(df["product_id"].count())

print("\nTop Product Categories:\n")

print(df["product_category_name"].value_counts().head(10))

import matplotlib.pyplot as plt

category_counts = df["product_category_name"].value_counts().head(10)

category_counts.plot(kind="bar")

plt.title("Top Product Categories")
plt.xlabel("Category")
plt.ylabel("Count")

plt.show()