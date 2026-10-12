#Pandas Mental Model
import pandas as pd

cpu = pd.Series([82, 55, 91])
print(cpu)
print(type(cpu))

df = pd.DataFrame({
    "service": ["payment", "orders", "inventory"],
    "cpu": [82, 55, 91]
})
print(df)
print(type(df))

#Part 2 — Creating DataFrames
# Dictionary of List
services = pd.DataFrame({
    "service": ["payment-api", "orders-api"],
    "cpu": [82, 55],
    "status": ["UP", "DOWN"]
})
print(services)

# List of Dictionary
services = pd.DataFrame([
    {"service": "payment-api", "cpu": 82, "status": "UP"},
    {"service": "orders-api", "cpu": 55, "status": "DOWN"}
])
print(services)


# Part 3 — Inspecting Data ⭐⭐⭐⭐⭐
services.head(1)
services.tail(1)
services.size
services.shape
services.columns
services.info()
services.describe()


#Part 4 — Column Selection ⭐⭐⭐⭐⭐
services["service"]
print(type(services["cpu"]))
services["cpu"]
services[["cpu", "service", "status"]]
print(type(services[["cpu", "service", "status"]]))


#Exercise D2-3
services = pd.DataFrame({
    "service": ["payment-api","orders-api","inventory-api","billing-api"],
    "cpu": [82,55,91,67],
    "memory": [71,60,84,52],
    "status": ["UP","DOWN","UP","UP"]
})
services[services["cpu"] > 80]
services[services["memory"] > 80]
services[services["status"] == "UP"]
services[(services["cpu"] > 80) & (services["status"] == "UP")]
services[(services["cpu"] > 80) | (services["memory"] > 80)]
services[services["status"] != "UP"]

#Part 7 — Sorting
services.sort_values("cpu", ascending=False)


#Part 8 — Creating / Modifying Columns
services["cpu_fraction"] = services["cpu"] / 100
print(services)
services["memory_fraction"] = services["memory"] / 100
print(services)
services["high_cpu"] = services["cpu"] > 80
print(services)
services["healthy"] = services["status"] == "UP"
print(services)

services["status"].value_counts()


# Day 2 Main Challenge
df = pd.read_csv("data/services.csv")
print(df)
df.head()
df[df["cpu"] > 80]
df.sort_values("cpu", ascending=False)
df["cpu"].mean()
df["status"].count()
df["cpu_fraction"] = df["cpu"] / 100
print(df)
df.to_csv("output/services-enriched.csv")