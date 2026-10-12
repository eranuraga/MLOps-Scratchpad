## Exercise 1 — Basic manipulation
services = [
    "payment-api",
    "orders-api",
    "inventory-api",
    "user-api"
]

#print the first service
print(services[0])

# Print the last service using negative indexing.
print(services[-1])

#Print the middle two services using slicing.
print(services[1:3])

#Add "billing-api" to the end.
services.append("billing-api")
print(services)

#Insert "auth-api" at index 1.
services.insert(1, "auth-api")
print(services)

#Remove "inventory-api" using remove().
services.remove("inventory-api")
print(services)

#Remove the last service using pop() and store the removed service in a variable.
popped_service = services.pop()
print(services)


#Delete the service at index 2 using del.
del services[2]

#Print the final list.
print(services)

#Print the value you removed using pop().
print(popped_service)


## Exercise 2 — append() vs extend()
## append will take the new list as is and will create a list inside a list as the last element in original list
## extend will extend the original list and add new values as the new elements in the list
services = ["payment-api", "orders-api"]

new_services = ["inventory-api", "billing-api"]

services.append(new_services)
print(services)

services.extend(new_services)
print(services)


## Exercise 3 — Sorting without destroying the original
##Requirement:
##The original latencies list must remain unchanged.
latencies = [250, 120, 450, 90, 310]

#Produce:
#Original:
#[250, 120, 450, 90, 310]
print(latencies)

#Ascending: [90, 120, 250, 310, 450]
sorted_latencies = sorted(latencies)
print(sorted_latencies)

#Descending:[450, 310, 250, 120, 90]
reverse_sorted_latencies = sorted(latencies, reverse=True)
print(reverse_sorted_latencies)

#Original:[250, 120, 450, 90, 310]
print(latencies)


##Exercise 4 — List copying trap
primary_services = [
    "payment-api",
    "orders-api",
    "inventory-api"
]

backup_services = primary_services

primary_services.append("billing-api")

print(primary_services)
print(backup_services)
## this is because .append is modifying the actual list
## use slicing to overcome this
backup_services = primary_services[:]
primary_services.append("billing-api")
print(primary_services)
print(backup_services)


##Exercise 5 — Looping through SRE data
services = [
    "payment-api",
    "orders-api",
    "inventory-api",
    "auth-api"
]

for service in services:
    print(f"Checking service: {service}")

for index, service in enumerate(services, start=1):
    print(index, service)
 


##Exercise 6 — Filtering
latencies = [120, 450, 80, 600, 210, 90, 510]
slow_requests = []
for latency in latencies:
    if latency > 300:
        slow_requests.append(latency)
print(slow_requests)


##Exercise 7 — Nested Lists
service_metrics = [
    ["payment-api", 82, 71],
    ["orders-api", 45, 60],
    ["inventory-api", 91, 84]
]

#Service: payment-api
#CPU: 82
#Memory: 71
for service in service_metrics:
     print(f"Service: {service[0]}")
     print(f"CPU: {service[1]}")
     print(f"Memory: {service[2]}")
     print("")
sum_cpu = 0
for cpus in service_metrics:
    sum_cpu += cpus[1]
average_cpu = sum_cpu / len(service_metrics)
print(f"Average CPU utilization: {average_cpu}")


## Exercise 8 — SRE Challenge ⭐⭐
services = [
    ["payment-api", "UP"],
    ["orders-api", "DOWN"],
    ["inventory-api", "UP"],
    ["billing-api", "DOWN"],
    ["auth-api", "UP"]
]
healthy_services = []
unhealthy_services = []

for service in services:
    if service[1] == "UP":
        healthy_services.append(service[0])
    else:
        unhealthy_services.append(service[0])
print(healthy_services)
print(unhealthy_services)
print(f"Total Services: {len(services)}")
print(f"Healthy Services: {len(healthy_services)}")
print(f"Unhealthy Services: {len(unhealthy_services)}")


## Exercise 9 — Final List Challenge 🔥
response_times = [
    120,
    340,
    89,
    450,
    230,
    600,
    110,
    95,
    510,
    180
]
#Total number of requests
print(len(response_times))

##Highest latency
max_response_time = response_times[0]
for seconds in response_times:
    if seconds > max_response_time:
        max_response_time = seconds

print(f"Highest latency: {max_response_time}")

##Lowest latency
min_response_time = response_times[0]
for time in response_times:
    if time < min_response_time:
        min_response_time = time

print(f"Lowest latency: {min_response_time}")

## Total latency
total_latency = 0
for times in response_times:
    total_latency +=times
print(f"Total latency: {total_latency}")


##Average latency
average = total_latency/len(response_times)
print(f"Average Latency: {average}")

## Number of requests > 300 ms
requests = 0
for i in response_times:
    if i > 300:
        requests +=1
print(f"Number of requests > 300 ms: {requests}")

## Percentage of requests > 300 ms
slow_request_percentage = requests/len(response_times)

print(f"Percentage of requests > 300 ms: {slow_request_percentage * 100}")

