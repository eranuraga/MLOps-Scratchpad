import requests

# We need coordinates to get weather data
latitude = 48.85   # Paris latitude
longitude = 2.35   # Paris longitude

# Build the API URL with our parameters
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

# Make the request
response = requests.get(url)
data = response.json()

print(data)

# type conversion: int(), float(), str(), bool()
cpu = "93.5"
cpu = float(cpu)

#None
pod_ip = None
if pod_ip is None:
    print("This is No Pod IP")
else:
    print(f"This is the pod ip {pod_ip}")

# isintsance() for checking the type of a variable
cpu_type = isinstance(cpu, float) # returns true or false


# if cpu_type == True:
# write
# if cpu_type:

# Instead of
# if len(cpu_type) == 0:
# write
# if not cpu_type:

#DICTIONARIES <-> JSON

cluster = {
"name":"dev-cluster",
"region":"us-ashburn-1",
"healthy":True,
"nodes":3,
"cpu":92.5,
"pods":["checkout","payment"]
}

print(f"Cluster Name: {cluster["name"]}")
print(f"CPU: {cluster["cpu"]}")
print(f"Number of Pods: {len(cluster['pods'])}") 
if cluster["healthy"]:
    print("The cluster is Healthy")

cluster["cpu"] = float(cluster["cpu"])
cluster["healthy"] = False
cluster["pods"].append("inventory")

print(cluster)

pods = [{
        "name": "checkout",
        "status": "Running"
    },
    {
        "name": "payment",
        "status": "CrashLoopBackOff"
    }]

print(pods[0]["name"])

for pod in pods:
    if pod["status"] == "CrashLoopBackOff":
     print(pod["name"])
