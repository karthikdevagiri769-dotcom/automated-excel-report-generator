import pandas as pd

print("STARTING SALES REPORT...")

# Read Excel file
df = pd.read_excel("sales_data.xlsx")

# Calculate sales
df["Total Sales"] = df["Quantity"] * df["Price"]

# Business calculations
total_revenue = df["Total Sales"].sum()

best_product = (
    df.groupby("Product")["Quantity"].sum().idxmax()
)

total_transactions = len(df)

highest_sale = df["Total Sales"].max()

# Display report
print("\n========== SALES REPORT ==========")

print(df)

print("\nTotal Revenue:", total_revenue)
print("Best Selling Product:", best_product)
print("Total Transactions:", total_transactions)
print("Highest Single Sale:", highest_sale)

# Export report
df.to_excel("sales_report.xlsx", index=False)

print("\nReport generated successfully!")