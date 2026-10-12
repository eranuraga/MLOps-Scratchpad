#Loading CSV Data
import pandas as pd

df = pd.read_csv("/Users/anurakuk/Desktop/python-for-ai/sre-incident-predictor/data/service_incidents.csv")
print(df.head())
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df["incident_next_hour"].value_counts())


# Data Validation
required_columns = {
    "cpu",
    "memory",
    "error_rate",
    "request_rate",
    "latency",
    "restart_count",
    "incident_next_hour"
}

print(set(df.columns))

missing_columns = required_columns - set(df.columns)
print(missing_columns)
if missing_columns:
    raise ValueError(
        f"Missing columns: {missing_columns}"
    )

print(
    df.isna().sum()
)
if df.isna().any().any():
    raise ValueError(
        "Dataset contains missing values"
    )

valid_targets = {0, 1}
actual_targets = set(
    df["incident_next_hour"].unique()
)
if not actual_targets.issubset(
    valid_targets):
    raise ValueError(
        f"Invalid targets: {actual_targets}"
    )


# Feature Preperation 
feature_columns = ["cpu","memory","error_rate","request_rate","latency","restart_count"]
target_column = "incident_next_hour"

X = df[feature_columns]
y = df[target_column]

print(X.shape)
print(y.shape)

print(X.head())
print(y.head())


# Train Test Split
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = (
    train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )
)

print(X_train.head())
print(X_test.head())

print(X_train.shape)
print(X_test.shape)

print(y_train.value_counts())
print(y_test.value_counts())


# Training
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=1000)
model.fit(X_train,y_train)


# Evaluation
predictions = model.predict(X_test)
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test,predictions)
print(f"Accuracy: {accuracy:.2%}")

comparison = pd.DataFrame({
"actual": y_test.values,
"predicted": predictions
})
print(comparison)


# Model artifact
import joblib

joblib.dump(model,"/Users/anurakuk/Desktop/python-for-ai/sre-incident-predictor/models/incident_model.joblib")


# Confusion Matrix
from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, predictions)
print(cm)

tn, fp, fn, tp = cm.ravel()

print(f"True Negative: {tn}")
print(f"False Positive: {fp}")
print(f"False Negative: {fn}")
print(f"True Positive: {tp}")

# Calculate Precision and Recall
from sklearn.metrics import precision_score, recall_score

precision = precision_score(y_test, predictions)
recall = recall_score(y_test, predictions)

print(f"Precision: {precision:.2%}")
print(f"Recall: {recall:.2%}")


#F1 Score
from sklearn.metrics import f1_score

f1 = f1_score(y_test, predictions)
print(f"F1 score: {f1:.2%}")


#Classification Report
from sklearn.metrics import classification_report

print(classification_report(y_test, predictions))