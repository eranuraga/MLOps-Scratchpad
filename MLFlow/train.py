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

mlflow.set_tracking_uri("http://127.0.0.1:5000")

mlflow.set_experiment(
    "sre-incident-predictor"
)

with mlflow.start_run():

    mlflow.log_params({
        "model_type": "LogisticRegression",
        "max_iter": 1000,
        "random_state": 42,
        "test_size": 0.2
    })
    from sklearn.linear_model import LogisticRegression
    model = LogisticRegression(max_iter=500)

    model.fit(
        X_train,
        y_train
    )

    predictions = model.predict(
        X_test
    )
    
    accuracy = accuracy_score(y_test,predictions)
    precision = precision_score(y_test, predictions)
    recall = recall_score(y_test, predictions)
    f1 = f1_score(y_test, predictions)

    mlflow.log_metrics({
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1": f1
    })

    mlflow.set_tag(
        "purpose",
        "baseline-classifier"
    )
    import json

    evaluation = {
    "accuracy": accuracy,
    "precision": precision,
    "recall": recall,
    "f1": f1
    }

    with open(
    "evaluation.json",
    "w"
    ) as f:
     json.dump(
        evaluation,
        f,
        indent=2
     )
    
    mlflow.log_artifact(
    "evaluation.json"
    )
    from mlflow.models import infer_signature
    signature = infer_signature(X_test, predictions)
    print(signature)
    input_example = X_test.iloc[[0]]
    print(input_example)

    model_info = mlflow.sklearn.log_model(
    sk_model=model,
    name="incident_model",
    signature=signature,
    input_example=input_example)

    print(model_info.model_uri)

    loaded_model = mlflow.sklearn.load_model(model_info.model_uri)
    loaded_predictions = loaded_model.predict(X_test)


    pyfunc_model = mlflow.pyfunc.load_model(model_info.model_uri)
    pyfunc_predictions = pyfunc_model.predict(X_test)
    print(predictions)
    print(loaded_predictions)
    print(pyfunc_predictions)

    result = mlflow.register_model(model_uri=model_info.model_uri, name="sre-incident-predictor")
    print(result.name)
    print(result.version)

    from mlflow import MlflowClient
    client = MlflowClient()
    client.set_registered_model_alias(
       name = "sre-incident-predictor",
       version="2",
       alias="candidate"
    )

    client.set_registered_model_alias(
       name="sre-incident-predictor",
       alias="champion",
       version="1"
    )

    model = mlflow.pyfunc.load_model(
       "models:/sre-incident-predictor@champion"
    )

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test,predictions)
    precision = precision_score(y_test, predictions)
    recall = recall_score(y_test, predictions)
    f1 = f1_score(y_test, predictions)
    
    mlflow.log_metrics({
            "accuracy": accuracy,
            "precision": precision,
            "recall": recall,
            "f1": f1
        })