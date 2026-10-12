def classify_service(services):
    if services["status"] == "DOWN":
        return "DOWN"
    elif (
        services["cpu"] > 90
        and services["error_rate"] > 0.05
    ):
        print(__name__)
        return "CRITICAL"
    elif (
        services["cpu"] > 80
        or services["error_rate"] > 0.05
    ):
        return "WARNING"
    else:
        return "HEALTHY"

if __name__ == "__main__":
    print("Testing health module")

    service = {
        "status": "DOWN"
    }

    print(classify_service(service))