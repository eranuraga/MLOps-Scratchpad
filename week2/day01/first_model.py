import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

#Load Dataset
df = pd.read_csv("data/service_incidents.csv")
print(df.head())
print(df.shape)

#Create X and Y
X = df[
    [
        "cpu",
        "memory",
        "error_rate",
        "request_rate",
        "latency",
        "restart_count"
    ]
]

y = df["incident_next_hour"]

#Splitting training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
print(X_train.shape)
print(X_test.shape)

print(y_train.shape)
print(y_test.shape)

#Creating model
model = LogisticRegression(max_iter=1000)

#Train Model
model.fit(X_train, y_train)
