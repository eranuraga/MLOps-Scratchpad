#Exercise1
def system_health(cpu):
 if cpu > 90:
    print("CRITICAL")
 elif cpu > 80:
    print("WARNING")
 else:
    print("HEALTHY")

system_health(87)
system_health(95)
system_health(82)
system_health(60)


#Exercise2
cpu = 92
error_rate = 0.02

if cpu > 90 and error_rate > 0.05 :
   print("CRITICAL")
elif cpu > 90 or error_rate > 0.05 :
   print("WARNING")
else:
   print("HEALTHY")


#Exercise3
services = [
    "payment-api",
    "orders-api",
    "inventory-api",
    "billing-api"
]

for service in services:
  print(f"Checking {service}")

for number,value in enumerate(services, start=1):
   print(str(number) + ". " + value)


#Exercise4
replicas = 5

for replica in range(1, replicas+1):
   print(f"Starting replica {replica}")


#Exercise5
services = [
    "payment-api",
    "orders-api",
    "inventory-api"
]

for number, value in enumerate(services, start=1):
   print(f"Service #{number} → {value}")


#Exercise6
attempt = 1
while attempt < 4:
   print(f"Health check attempt {attempt}")
   attempt += 1

attempt = 1
while attempt < 3:
   print(f"Health check attempt {attempt}")
   attempt += 1
print("Health check succeeded")


#Exercise7
incidents = [
    {"service": "orders-api", "severity": "P3"},
    {"service": "billing-api", "severity": "P2"},
    {"service": "inventory-api", "severity": "P1"},
    {"service": "payment-api", "severity": "P1"}
]

for incident in incidents:
   if incident["severity"] == "P1":
      print(f"P1 found: {incident["service"]}")
      break


#Exercise8
services = [
    {"name": "payment-api", "enabled": True},
    {"name": "orders-api", "enabled": False},
    {"name": "inventory-api", "enabled": True}
]

for service in services:
   if service["enabled"] == False:
      continue
   print(f"Checking {service["name"]}")


#Exercise9
services = {
    "payment-api": ["pod-1", "pod-2"],
    "orders-api": ["pod-1", "pod-2", "pod-3"],
    "inventory-api": ["pod-1"]
}

for service, pods in services.items():
   print(service)
   for pod in pods:
      print(pod)


# Day4 Mini Challenge
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
down_service = []
critical_service = []
warning_service = []
healthy_service = []
for service in services:
   if service["status"] == "DOWN":
      print(f"{service["name"]} -> DOWN")
      down_service.append(service["name"])
   elif service["cpu"] > 90 and service["error_rate"] > 0.05:
      print(f"{service["name"]} -> CRITICAL")
      critical_service.append(service["name"])
   elif service["cpu"] > 80 or service["error_rate"] > 0.05:
      print(f"{service["name"]} -> WARNING")
      warning_service.append(service["name"])
   else:
      print(f"{service["name"]} -> HEALTHY")
      healthy_service.append(service["name"])

print(f"Total services {len(services)}")
print(f"Healthy services count {len(healthy_service)}")
print(f"Warning services count {len(warning_service)}")
print(f"Critical services count {len(critical_service)}")
print(f"Down services count {len(down_service)}")