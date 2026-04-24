import pandas as pd
df = pd.read_excel(r"C:\Users\ACS\Desktop\blinkit\blinkit_customers.xlsx")
# print(df)
p=df.groupby("customer_segment").agg({"avg_order_value":"sum"}).sort_values("avg_order_value",ascending=False)
print(p)


