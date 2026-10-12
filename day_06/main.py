from app.health import classify_service
from app.incidents import count_incidents
from app.metrics import calculate_error_rate


services = [
    {
        "name": "payment-api",
        "cpu": 92,
        "error_rate": 0.07,
        "status": "UP",
        "severity": "P1"
    }
    ]

for service in services:
    status = classify_service(service)
    print(f"{status}")
