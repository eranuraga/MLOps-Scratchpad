from health import classify_service
service = {
    "name": "payment-api",
    "cpu": 92,
    "error_rate": 0.07,
    "status": "UP"
}
result = classify_service(service)
print(result)

