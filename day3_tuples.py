a = ("payment-api")
b = ("payment-api",)

print(type(a))
print(type(b))

## Exercise 1
service = ("payment-api", "production", "UP", 5)
#Print the service name, environment, last element using negative indexing, and the first two elements using slicing.
print(f"Service Name: {service[-4]}")
print(f"Environment: {service[-3]}")
print(f"Last Element: {service[-1]}")
print(f"First 2 elements: {service[0:2]}")


## Exercise 2
name, environment, status, replicas = service
print(f"Service: {name}")
print(f"Environment: {environment}")
print(f"Status: {status}")
print(f"Replicas: {replicas}")


##Exercise T3: Try modifying status directly inside the tuple. Record the exception and explain why Python raises it.
service[2] = "DOWN"
print(service)
## Tuple object does not support item assignment


##Exercise 4:
services = [
    ("payment-api", "UP"),
    ("orders-api", "DOWN"),
    ("inventory-api", "UP")
]
##Use tuple unpacking directly in the loop:

for service in services:
    print(f"{service[0]}: {service[1]}")


##If somehow we have defined a list inside a tuple then that list is mutable 


##Tuple unpacking
service_metrics = [
    ("payment-api", 82, 71),
    ("orders-api", 45, 60),
    ("inventory-api", 91, 84)
]

for service, cpu, memory in service_metrics:
    print(f"Service: {service}, CPU: {cpu}, Memory: {memory}")

