#Exercise1
from pathlib import Path

filepath = Path("data/incidents.json")
print(filepath)
print(type(filepath))

if filepath.exists():
    print("File Exists")
else:
    print("File is missing")

print(filepath.name)
print(filepath.parent)


#Exercise2
with open("data/services.txt","r") as file:
    content = file.read()

print(content)
print(type(content))
#.read() returned string

#Exercise3
services = []
with open("data/services.txt", "r") as file:
     for line in file:
         services.append(line.strip())
print(services)

#Exercise4
with open("output/health.txt", "w") as file:
    service_health = ["payment-api: HEALTHY", "orders-api: WARNING","inventory-api: CRITICAL"]
    for service in service_health:
      file.writelines(service + "\n")

with open("output/health.txt", "a") as file:
    file.write("billing-api: HEALTHY")


#Exercise5
def read_file(path:str):
        with open(path,"r") as file:
            return file.read()

try:
    content = read_file("output/health.txt")
except FileNotFoundError as exc:
    print(f"File not found: {exc}")
else:
    print(content)

#Exercise J1
json_string = """
{
    "service": "payment-api",
    "severity": "P1",
    "status": "OPEN"
}
"""
import json
services = json.loads(json_string)
print(services)
print(type(services))
print(services.get("service"))
print(services.get("severity"))
print(services.get("status"))

#Exercise J2
summary = {
    "total_services": 4,
    "healthy": 2,
    "warning": 1,
    "critical": 1
}
summary_string = json.dumps(summary, indent=4)
print(summary_string)
print(type(summary_string))

#ExericseJ3
with open("data/incidents.json", "r") as file:
    incidents = json.load(file)
     
print(f"Total incidents: {len(incidents)}")
count_p1 = 0
for incident in incidents:
    print(f'Services are: {incident.get("service")}')
    if incident.get("severity") == "P1":
        count_p1 += 1
print(f"Count of P1 severity services are: {count_p1}")


#ExerciseJ4
summary = {}
summary["total_incidents"] = len(incidents)
summary["p1_incidents"] = count_p1
print(summary)

#Exercise J5 — Robust JSON Loader
def load_incidents(path):
    with open(path, "r") as file:
        return json.load(file)

try:
    print(load_incidents("data/incidents.json"))
except FileNotFoundError as excp:
    print(f"File not found error: {excp}")
except json.JSONDecodeError as excp:
    print(f"This doesn't seems to be a correct Json: {excp}")


##🔥 Session 1 Main Challenge
with open("data/incidents.json", "r") as file:
    incident_python = json.load(file)
print(f"Total incidents are: {len(incident_python)}")

by_severity = {}
severity_list = []
for incident in incident_python: 
   severity_list.append(incident["severity"])
print(severity_list)
count = 0
for severity in severity_list:
       if severity not in severity_list:
           count += 1
       else:
           count = 1
           
print(by_severity)














    

    
