#Exercise2

def check_service(service, environment):
    print(f"Checking {service} in {environment}")

check_service(
    "payment-api",
    "production"
)


#Exercise3

def calculate_error_rate(errors, requests):
    return errors / requests

rate = calculate_error_rate(5, 100)

print(rate)
if rate > 0.03:
    print("WARNING")


#Refactor Your Health Classifier
def classify_service(cpu, error_rate, status):
    if status == "DOWN":
        return "DOWN"
    elif cpu > 90 and error_rate > 0.05 :
        return "CRITICAL"
    elif cpu > 90 or error_rate > 0.05 :
        return "WARNING"
    else:
        return "HEALTHY"

health = classify_service(
    92,
    0.07,
    "UP"
)

print(health)


#Exercise4
def service_info(name, environment, replicas):
    print(f"The name of service is {name}")
    print(f"It is in environment {environment}")
    print(f"There are {replicas} replicas")

service_info("payment-api", "production", 5 )
service_info(
    replicas=5,
    name="payment-api",
    environment="production"
)


#Exercise5
def create_alert(service,severity="P3"):
    print(f"Service is {service} with severity {severity}")

create_alert("payment-api")
create_alert("payment-api","P1")


#Exercise6
def analyze_requests(total_requests, failed_requests):
    successful_requests = total_requests - failed_requests
    error_rate = failed_requests / total_requests
    return successful_requests, error_rate 

successful, error_rate = analyze_requests(
    1000,
    25
)

print(successful)
print(error_rate)


#Scope
def calculate():
    result = 10
    print(result)

calculate()

print(result)

## Python Type Hints
def calculate_error_rate(errors: int, requests: int) -> float:
    return errors / requests

calculate_error_rate(2.43,5.69)

## Docstrings
def calculate_error_rate(
    errors: int,
    requests: int
) -> float:
    """Calculate the fraction of failed requests."""
    return errors / requests


#Day 5 Main Challenge — Refactor Your SRE Health Checker
services = [
    {
        "name": "payment-api",
        "cpu": 92,
        "error_rate": 0.07,
        "status": "UP"
    },
    {
        "name": "orders-api",
        "cpu": 55,
        "error_rate": 0.01,
        "status": "UP"
    },
    {
        "name": "inventory-api",
        "cpu": 88,
        "error_rate": 0.03,
        "status": "DOWN"
    },
    {
        "name": "billing-api",
        "cpu": 72,
        "error_rate": 0.06,
        "status": "UP"
    }
]

def classify_service(service):
    if service["status"] == "DOWN":
        return "DOWN"
    elif service["cpu"] > 90 and service["error_rate"] > 0.05 :
        return "CRITICAL"
    elif service["cpu"] > 90 or service["error_rate"] > 0.05 :
        return "WARNING"
    else:
        return "HEALTHY"

for service in services:
    health = classify_service(service)
    print(f"{service["name"]} is in {health} state")


#Challenge2

incidents = [
    {"service": "payment-api", "severity": "P1"},
    {"service": "orders-api", "severity": "P2"},
    {"service": "payment-api", "severity": "P1"},
    {"service": "inventory-api", "severity": "P3"},
    {"service": "orders-api", "severity": "P1"},
    {"service": "payment-api", "severity": "P2"}
]

def count_incidents(incidents,field):
    count = {}
    for incident in incidents:
        field_value = incident[field] 
        if field_value in count:
            count[field_value] += 1
        else:
            count[field_value] = 1
    return(count)

service_count = count_incidents(
    incidents,
    "service"
)
print(service_count)

severity_count = count_incidents(
    incidents,
    "severity"
)
print(severity_count)
