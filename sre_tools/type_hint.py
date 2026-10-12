def get_service_owner(service: dict,) -> str | None:
    return service.get("owner")

service = {
    "name": "payment-api",
    "owner": "platform-team"
}

get_service_owner(service)

service = {
    "name": "payment-api"
}
get_service_owner(service)