import pandas as pd
blinkit_customers= pd.read_excel(r"C:\Users\ACS\Desktop\blinkit\blinkit_customers.xlsx")
# print(blinkit_customers)
p=blinkit_customers.groupby("customer_segment").agg({"avg_order_value":"sum"}).sort_values("avg_order_value",ascending=False)
# print(p)

blinkit_orders= pd.read_excel(r"C:\Users\ACS\Desktop\blinkit\blinkit_orders.xlsx")

blinkit_orders["date"]=blinkit_orders["order_date"].dt.date
blinkit_orders["time"]=blinkit_orders["order_date"].dt.time
# Which customer segments (Premium, Regular, Inactive) generate most revenue?

most_revenue_customers = pd.merge(blinkit_customers,blinkit_orders,on="customer_id").groupby("customer_segment").agg({"order_total":"sum"}).sort_values("order_total",ascending=False)
print(most_revenue_customers)

# Find inactive customers we can reactivate.

merged_data = pd.merge(blinkit_customers, blinkit_orders, on="customer_id", how="outer")
inactive_customers = merged_data[merged_data["customer_segment"] == "Inactive"]["customer_id"].unique()
print(inactive_customers)
ko54ogl4imglk4o5jtik4jm6go




