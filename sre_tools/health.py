def classify_service(service):
    if service["status"] == "DOWN":
        return "DOWN"
    elif service["cpu"] > 90 and service["error_rate"] > 0.05 :
        return "CRITICAL"
    elif service["cpu"] > 90 or service["error_rate"] > 0.05 :
        return "WARNING"
    else:
        return "HEALTHY"

print("Testing health module")
print(__name__)