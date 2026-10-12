from app.incidents import validate_incident
from app.exceptions import InvalidIncidentError
incidents = [
    {
        "service": "payment-api",
        "severity": "P1",
        "status": "OPEN"
    },
    {
        "service": "orders-api",
        "severity": "P9",
        "status": "OPEN"
    },
    {
        "service": "inventory-api",
        "severity": "P2"
    }
]

for incident in incidents:
    try:
        validate_incident(incident)

    except InvalidIncidentError as exc:
        print(
            f"Invalid incident: {exc}"
        )

    else:
        print(
            "Incident valid"
        )