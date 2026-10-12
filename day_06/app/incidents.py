from .exceptions import InvalidIncidentError
def count_incidents(incidents:list[dict[str]],field: str) -> dict[str, int]:
    count = {}
    for incident in incidents:
        field_value = incident[field] 
        if field_value in count:
            count[field_value] += 1
        else:
            count[field_value] = 1
    return(count)

def validate_incident(incident):
    valid_keys = ["service","severity","status"]
    incident_keys = incident.keys()
    for key in incident_keys:
        if key not in valid_keys:
            raise InvalidIncidentError(f"Unexpected key: {key}")

    if incident.get("severity") not in {"P1", "P2", "P3"}:
        raise InvalidIncidentError(f'invalid severity: {incident["severity"]}')