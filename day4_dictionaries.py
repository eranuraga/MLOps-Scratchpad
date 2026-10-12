## Udemy Exercise for Dictionary
sample_dict = {
    "mouth": "Mund",
    "finger": "Finger",
    "leg": "Bein",
    "hand": "Hand",
    "face": "Gesicht",
    "nose": "Nase"
}

while True:
    word = input('Enter a word in English or EXIT: ')
    
    if word == 'EXIT':
         print("Bye!")
         break
    elif word in sample_dict:
      print('Translation:', sample_dict[word])
    else:
      print('No match!')


## Other sets of examples

service = {
    "name": "payment-api",
    "environment": "production",
    "status": "UP",
    "cpu": 82,
    "memory": 71
}
## type of dictionary and length
print(type(service))
print(len(service))

## Keys doesnt exist for simulating key error
print(service["region"])

## Use of get for a key that doesn't exist
## and then assigning default value as "unknown"

print(service.get("region", "unknown"))

# Exercise1
service = {
    "name": "payment-api",
    "environment": "production",
    "cpu": 82,
    "memory": 71,
    "replicas": 4
}

#Print service name.
print(service["name"])
#Print CPU.
print(service["cpu"])
#Print number of key/value pairs.
print(len(service))
#Change CPU from 82 → 90.
service["cpu"] = 90
print(service)
#Change replicas from 4 → 6.
service["replicas"] = 6
print(service)
#Add "status": "UP".
service.update({"status": "UP"})
print(service)
#Add "region": "ap-south-1".
service["region"] = "ap-south-1"
print(service)
##Remove region using del.
del service["region"]
##Remove status using pop() and store its value.
popped_value = service.pop("status")
#Print the removed status.
print(popped_value)
#Print the final dictionary.
print(service)

## Exercise2
service = {
    "name": "payment-api",
    "environment": "production",
    "cpu": 82,
    "memory": 71,
    "replicas": 4
}

for key, values in service.items():
   print(key + ' = ' + str(values))

## Exercise3
service = {
    "name": "payment-api",
    "environment": "production",
    "metrics": {
        "cpu": 82,
        "memory": 71,
        "error_rate": 0.03
    }
}
#Print service name.
print(service["name"])
#Print environment.
print(service["environment"])
#Print CPU.
print(service["metrics"]["cpu"])
#Print memory.
print(service["metrics"]["memory"])
#Change CPU → 95.
service["metrics"]["cpu"] = 95
#Add latency → 240.
service["metrics"]["latency"] = 240
#Loop over metrics and print:
metrics = service["metrics"]
for key,values in metrics.items():
   print(key + ":" + str(values))


# Exericse 4
services = [
    {
        "name": "payment-api",
        "cpu": 82,
        "status": "UP"
    },
    {
        "name": "orders-api",
        "cpu": 45,
        "status": "DOWN"
    },
    {
        "name": "inventory-api",
        "cpu": 91,
        "status": "UP"
    },
    {
        "name": "billing-api",
        "cpu": 67,
        "status": "UP"
    }
]

#Total services
print(f"Total Services: {len(services)}")
#Number of UP services
#Number of DOWN services
#Names of UP services
up_service = 0
down_service = 0
up_service_name = []
service_high_cpu = []
for service in services:
   if service["status"] == "UP":
      up_service += 1
      
   elif service["status"] == "DOWN":
      down_service += 1
print(f"Total UP service: {up_service}")
print(f"Total DOWN service: {down_service}")
print(f"Up service names: {up_service_name}")

#Names of services with CPU > 80
high_cpu_service = []
for service in services:
   if service["cpu"] > 80:
      high_cpu_service.append(service["name"])
print(f"Services with CPU greater than 80%: {high_cpu_service}")


#Service with highest CPU

## Exercise 5
incidents = [
    {"service": "payment-api", "severity": "P1"},
    {"service": "orders-api", "severity": "P2"},
    {"service": "payment-api", "severity": "P1"},
    {"service": "inventory-api", "severity": "P3"},
    {"service": "orders-api", "severity": "P1"},
    {"service": "payment-api", "severity": "P2"}
]

count = {}
for incident in incidents:
   service = incident["service"]
   if service in count:
      count[service] +=1
   else:
      count[service] = 1
print(count)

count_severity = {}
for incident in incidents:
   severity = incident["severity"]
   if severity in count_severity:
      count_severity[severity] +=1
   else:
      count_severity[severity] = 1
print(count_severity)



