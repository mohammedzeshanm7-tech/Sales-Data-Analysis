import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("sales_data.csv")

print(data.head())

sales_by_country = data.groupby("COUNTRY")["SALES"].sum()

sales_by_country.plot(kind="bar", figsize=(10,6))
plt.title("Total Sales by Country")
plt.xlabel("Country")
plt.ylabel("Sales")
plt.show()
