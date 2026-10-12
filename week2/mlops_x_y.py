import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

df = pd.read_csv("data/service_incidents.csv")
print(df.head())
print(df.shape)
print(df.columns)
df["incident_next_hour"].value_counts()

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

print(X.shape)
print(y.shape)
print(X.head())
print(y.head())

print(X)
print(y.value_counts())

X_train, X_test, y_train, y_test = (
    train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )
)

print(X_train.shape)
print(X_test.shape)

print(y_train.shape)
print(y_test.shape)

print(y_train.value_counts())
print(y_test.value_counts())

model = LogisticRegression(max_iter=1000)
print(model)

model.fit(X_train, y_train)

predictions = model.predict(
    X_test
)

print(predictions)
print(y_test.values)

comparison = pd.DataFrame({
    "actual": y_test.values,
    "predicted": predictions
})

print(comparison)

accuracy = accuracy_score(
    y_test,
    predictions
)
print(
    f"Test Accuracy: {accuracy * 100:.2f}%"
)


train_predictions = model.predict(
    X_train
)

train_accuracy = accuracy_score(
    y_train,
    train_predictions
)

test_accuracy = accuracy_score(
    y_test,
    predictions
)

print(
    f"Training Accuracy: "
    f"{train_accuracy * 100:.2f}%"
)

print(
    f"Test Accuracy: "
    f"{test_accuracy * 100:.2f}%"
)

probabilities = model.predict_proba(
    X_test
)

print(probabilities)

print(
    model.predict_proba(X_test)[:, 1]
)

new_service = pd.DataFrame([
    {
        "cpu": 94,
        "memory": 87,
        "error_rate": 0.08,
        "request_rate": 1300,
        "latency": 480,
        "restart_count": 4
    }
])

prediction = model.predict(
    new_service
)

print(prediction)

probability = model.predict_proba(
    new_service
)[:, 1]

print(probability)