services = {
    "payment-api",
    "orders-api",
    "payment-api"
}

print(services)

## defining service
services = set()
print(type(services))

## adding values
services.add("billing-api")
services.add("billing-api")
print(services)

## removing values
services.remove("billing-api")
print(services)

## Membership
critical_services = {
    "payment-api",
    "inventory-api"
}
print("payment-api" in critical_services)
print("orders-api" in critical_services)

## Exercise1
affected_services = [
    "payment-api",
    "orders-api",
    "payment-api",
    "inventory-api",
    "orders-api",
    "payment-api"
]

affected_set = set(affected_services)
print(affected_set)

affected_list = list(affected_set)
print(affected_list)

## Exercise2 - Union
alerting_services = {
    "payment-api",
    "orders-api",
    "inventory-api"
}

recently_deployed = {
    "payment-api",
    "billing-api",
    "inventory-api"
}

print(alerting_services | recently_deployed)
alerting_services.union(recently_deployed)

## Exercise3 - Intersection
alerting_services = {
    "payment-api",
    "orders-api",
    "inventory-api"
}

recently_deployed = {
    "payment-api",
    "billing-api",
    "inventory-api"
}

alerting_services.intersection(recently_deployed)
list_deployment_related_incidents = list(alerting_services.intersection(recently_deployed))

print(list_deployment_related_incidents)
print("Potential deployment-related incidents: ")
for incidents in list_deployment_related_incidents:
    print(incidents)


critical = {
    "payment-api",
    "inventory-api"
}

all_services = {
    "payment-api",
    "inventory-api",
    "orders-api",
    "billing-api"
}

critical.issubset(all_services)
all_services.issuperset(critical)

alerting_services = {
    "payment-api",
    "orders-api",
    "inventory-api"
}

recently_deployed = {
    "payment-api",
    "billing-api",
    "inventory-api"
}

critical_services = {
    "payment-api",
    "inventory-api"
}
# all services involved
print(alerting_services.union(recently_deployed))
#Services that are alerting AND recently deployed
print(alerting_services.intersection(recently_deployed))
#Services alerting but not deployed
print(alerting_services - recently_deployed)
#Recently deployed but not alerting
print(recently_deployed - alerting_services)
#Services that are both critical AND recently deployed
print(recently_deployed.intersection(critical_services))
#Services that are critical AND alerting
print(critical_services.intersection(alerting_services))


#Final Challenge
services = [
    {
        "name": "payment-api",
        "status": "UP",
        "cpu": 92
    },
    {
        "name": "orders-api",
        "status": "UP",
        "cpu": 55
    },
    {
        "name": "inventory-api",
        "status": "DOWN",
        "cpu": 88
    },
    {
        "name": "billing-api",
        "status": "UP",
        "cpu": 40
    }
]

recently_deployed = {
    "payment-api",
    "inventory-api"
}

#Total Services: 4
print(f"Total Services: {len(services)}")

#Down Services:
#inventory-api
print("Down Services:")
down_services = []
for service in services:
    if service["status"] == "DOWN":
        down_services.append(service["name"])
for down_service in down_services:
    print(down_service)

#High CPU Services:
#payment-api
#inventory-api
high_cpu_services = []
for service in services:
   if service["cpu"] > 80:
       high_cpu_services.append(service["name"])
print(high_cpu_services)
for high_cpu in high_cpu_services:
    print(high_cpu)

##Recently Deployed:
#payment-api
#inventory-api
recently_deployed_list = list(recently_deployed)
for recent_deployed in recently_deployed_list:
    print(recent_deployed)

#High CPU + Recently Deployed:
#payment-api
#inventory-api
high_cpu_recent_deploy = (set(high_cpu_services).intersection(recently_deployed))
high_cpu_recent_deploy_list = list(high_cpu_recent_deploy)
for service in high_cpu_recent_deploy_list:
    print(service)

#Potential Deployment-Related Incident:
for down_service in down_services:
    print(down_service)