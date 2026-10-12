#Exercise1
def calculate_error_rate(errors, requests):
    try:
        return errors / requests
    except ZeroDivisionError:
        return 0.0

print(calculate_error_rate(5, 100))

print(calculate_error_rate(5, 0))

#Exercise2
service = {
    "name": "payment-api",
    "environment": "production"
}

try:
    service["region"]
except KeyError as excp:
    print(excp)

print(service.get("region"))

#Exercise3
def calculate_per_replica_load(total_load, replicas):
   try:
      load = total_load / replicas
      return load
   except TypeError:
       print("Values must be integers")
   except ZeroDivisionError:
       print("Replicas value can't be 0")

calculate_per_replica_load(1000, 5)
calculate_per_replica_load('asd', 0)


##Exercise4
def process_replica_count(value):
    try:
        replica_count = int(value)
    except ValueError:
        print("Invalid replica count")
    else:
        print(f"Replica count: {replica_count}")
    finally:
        print("Processing completed")

process_replica_count("5")
process_replica_count("hello")

##Exercise5
def validate_severity(severity):
    if severity not in {"P1", "P2", "P3"}:
            raise ValueError(f"Invalid severity: {severity}")
    else:
        return True

validate_severity("P1")
validate_severity("P9")


#Exercise6
class InvalidIncidentError(Exception):
    pass

def validate_incident(incident):
    valid_keys = ["service","severity","status"]
    incident_keys = incident.keys()
    for key in incident_keys:
        if key not in valid_keys:
            raise InvalidIncidentError(f"{key} is not a valid key")
    if len(incident) != 3:
        raise InvalidIncidentError("we need exactly 3 keys but looks like some keys are missing")
incident = {
    "service": "payment-api",
    "severity": "P1"
}

validate_incident(incident)
