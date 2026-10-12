import pandas as pd
import mlflow
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

df = pd.read_csv("/Users/anurakuk/Desktop/python-for-ai/MLFlow/data/service_incidents.csv")

# Feature Preperation 
feature_columns = ["cpu","memory","error_rate","request_rate","latency","restart_count"]
target_column = "incident_next_hour"

X = df[feature_columns]
y = df[target_column]

# Train Test Split
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

from sklearn.linear_model import LogisticRegression

mlflow.sklearn.autolog()

with mlflow.start_run():

    model = LogisticRegression(
        max_iter=1000,
        random_state=42
    )

    model.fit(
        X_train,
        y_train
    )