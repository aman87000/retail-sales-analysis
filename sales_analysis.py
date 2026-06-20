import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("sales data.csv", encoding="cp1252")

# Dataset Info
print("===== DATASET INFO =====")
print("Rows and Columns:", df.shape)

print("\n===== FIRST 5 ROWS =====")
print(df.head())

# Total Sales
print("\n===== TOTAL SALES =====")
print(df["Sales"].sum())

# Total Profit
print("\n===== TOTAL PROFIT =====")
print(df["Profit"].sum())

# Sales by Category
print("\n===== SALES BY CATEGORY =====")
sales_category = df.groupby("Category")["Sales"].sum()
print(sales_category)

# Profit by Category
print("\n===== PROFIT BY CATEGORY =====")
profit_category = df.groupby("Category")["Profit"].sum()
print(profit_category)

# Top 10 Products
print("\n===== TOP 10 PRODUCTS =====")
top_products = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
print(top_products)

# Top 10 Customers
print("\n===== TOP 10 CUSTOMERS =====")
top_customers = (
    df.groupby("Customer Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
print(top_customers)

# Convert Date Column
df["Order Date"] = pd.to_datetime(
    df["Order Date"],
    format="mixed",
    errors="coerce"
)

# Monthly Sales Trend
monthly_sales = df.groupby(df["Order Date"].dt.month)["Sales"].sum()

print("\n===== MONTHLY SALES =====")
print(monthly_sales)

# -------------------
# Chart 1
# -------------------
plt.figure(figsize=(6,4))
sales_category.plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("sales_by_category.png")
plt.show()

# -------------------
# Chart 2
# -------------------
plt.figure(figsize=(6,4))
profit_category.plot(kind="bar")
plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.tight_layout()
plt.savefig("profit_by_category.png")
plt.show()

# -------------------
# Chart 3
# -------------------
plt.figure(figsize=(8,4))
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.tight_layout()
plt.savefig("monthly_sales_trend.png")
plt.show()

print("\nPROJECT COMPLETED SUCCESSFULLY")