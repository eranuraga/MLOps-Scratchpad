import pandas as pd

cpu = pd.Series([
    82,
    55,
    91,
    67,
    88
])

print(cpu)
print(type(cpu))
print(cpu.size)
print(cpu.shape)
print(cpu.dtype)


## Data Frame
services = pd.DataFrame({
    "service": [
        "payment-api",
        "orders-api",
        "inventory-api",
        "billing-api",
        "auth-api"
    ],
    "cpu": [
        82,
        55,
        91,
        67,
        88
    ],
    "memory": [
        71,
        60,
        84,
        52,
        79
    ],
    "latency": [
        120,
        340,
        450,
        180,
        510
    ],
    "status": [
        "UP",
        "DOWN",
        "UP",
        "UP",
        "UP"
    ]
})

print(type(services))
print(services.shape)
print(services.size)
print(services.columns) 
print(services.dtypes)

#EDA
print(services.head())
print(services.tail(3))
print(services.info())
print(services.describe())

print(services["cpu"])
print(services[["cpu", "memory"]])

print(services.iloc[0,:])
print(services.iloc[2,:])
print(services.iloc[-1, :])
print(services.iloc[0:2, :])
print(services.iloc[0:3, 0:2])
print(services.iloc[:,1])

print(services.iloc[2,1])
print(services.loc[2,"cpu"])

print(services[services["cpu"] > 80])
print(services[services["memory"] > 70])
print(services[services["latency"] > 300])
print(services[services["status"] == "UP"])
print(services[services["status"] != "UP"])

print(services.loc[
    services["cpu"] > 80,
    "service"
])


## Final Challenge
import pandas as pd

services = pd.DataFrame({
    "service": [
        "payment-api",
        "orders-api",
        "inventory-api",
        "billing-api",
        "auth-api",
        "search-api"
    ],
    "team": [
        "payments",
        "commerce",
        "platform",
        "payments",
        "platform",
        "commerce"
    ],
    "cpu": [
        82,
        55,
        91,
        67,
        88,
        73
    ],
    "memory": [
        71,
        60,
        84,
        52,
        79,
        66
    ],
    "latency": [
        120,
        340,
        450,
        180,
        510,
        290
    ],
    "status": [
        "UP",
        "DOWN",
        "UP",
        "UP",
        "UP",
        "DOWN"
    ]
})

print(services.shape)
print(services.size)
print(services.columns)
print(services.dtypes)
print(services.info())
print(services.head(3))
print(services.describe())

print(services["cpu"]) #series
print(services["service"]) #series
print(services[["service", "cpu"]]) #dataframe
print(services[["cpu", "memory", "latency"]]) #dataframe

print(services.iloc[0,:])
print(services.iloc[2,:])
print(services.iloc[-1,:])
print(services.iloc[0:3,:])
print(services.loc[2, "cpu"])
print(services.loc[0:2, ["cpu", "service"]])

print(services[services["cpu"] > 80])
print(services[services["latency"] > 300])
print(services[services["status"] == "UP"])
print(services[(services["cpu"] > 80) & (services["latency"] > 300)])
print(services[(services["cpu"] > 70) & (services["latency"] > 400)])

print(services.loc[services["cpu"] > 80, "service"])
print(services.loc[services["latency"] > 300, ["service", "latency"]])

print(services.sort_values("cpu", ascending=False))
print(services.sort_values("latency", ascending=False))

services["cpu_fraction"] = services["cpu"] / 100
services["memory_fraction"] = services["memory"] / 100
services["latency_seconds"] = services["latency"] / 1000
services["high_cpu"] = services["cpu"] > 80
services["high_latency"] = services["latency"] > 300
services["healthy"] = services["status"] == "UP"

print(services)

print(services["cpu"].mean())
print(services["memory"].mean())
print(services["latency"].mean())

print(services["cpu"].max())
print(services["latency"].max())

print((services["status"] == "UP").sum())
print((services["status"] == "DOWN").sum())

print((services["cpu"] > 80).mean())
print((services["latency"] > 300).mean())


#Pandas Day2
import pandas as pd

services = pd.DataFrame({
    "service": [
        "payment-api",
        "orders-api",
        "inventory-api",
        "billing-api",
        "auth-api"
    ],
    "team": [
        "payments",
        "commerce",
        "platform",
        "payments",
        "platform"
    ],
    "cpu": [
        82,
        None,
        91,
        67,
        88
    ],
    "memory": [
        71,
        60,
        None,
        52,
        79
    ],
    "status": [
        "UP",
        "DOWN",
        "UP",
        "UP",
        None
    ]
})

services.isna()
services.isna().sum()

services[
    services.isna().any(axis=1)
]

print(services.dropna())


clean_services = services.copy()
clean_services["cpu"] = (clean_services["cpu"].fillna(clean_services["cpu"].median()))
print(clean_services)
clean_services["memory"] = clean_services["memory"].fillna(clean_services["memory"].median())
print(clean_services)
clean_services["status"] = clean_services["status"].fillna("UNKNOWN")
print(clean_services)