import joblib

model = joblib.load(
    "/Users/anurakuk/Desktop/python-for-ai/sre-incident-predictor/models/incident_model.joblib"
)

print(model)