name = input("Enter your name: ")
age = int(input("Enter your age please: "))
college = (input("Enter your college: "))
branch = (input("Enter your branch: "))


print("------ Student Details ------")
print(f"Name.   : {name}")
print(f"Age.    : {age}")
print(f"College : {college}")
print(f"Branch  : {branch}")

print("Welcome to Coffee Shop")
print("")
print("")
cust_name = input("Enter customer name:")
price = float(input("Enter coffee price:"))
quantity = int(input("Enter quantity:"))

print("----------- RECEIPT -----------")
print(f"Customer : {cust_name}")
print(f"Price    : {price}")
print(f"Quantity : {quantity}")
print(f"Total    : {price * quantity}")
print("Thank you!")




# num1 = int(input("Please enter first number: "))
# num2 = int(input("Now enter second number: "))           
# print(f"Addition of {num1} and {num2} is {num1+ num2}")


payment = "payment-76f98c9d6b-x2msl"
print(len(payment))
print(payment.lower())
print(payment.upper())
print(payment.replace("payment", "orders"))

pods = [
    "payment",
    "frontend",
    "orders",
    "inventory"
]
print(pods[0])
print(pods[-1])
print(pods[1])
print(len(pods))

pods.append("shipping")
print(pods)
(pods.remove("frontend"))
print(pods)

cluster = {
    "name": "production",
    "pods": [
        "payment",
        "frontend",
        "orders"
    ]
}

print(f"Cluster Name :{cluster.get("name")}")
print(f"Total Pods : {len(cluster.get("pods"))}")
print(f"First Pod : {cluster.get("pods")[0]}")


days = int(input("How many days ago you have purchased the item: "))
is_used = input("Is the item used [y/n]: ")
is_broken = input("Has the item broken on its own [y/n]: ")

if (is_broken == "y" or (days <= 10 and is_used == "n")):
    print("You are eligible for refund")
else:
    print("You will not get refund")



service = "payment-api"
replicas = 5
error_rate = 0.023
healthy = True
owner = None

print(service, replicas, error_rate, healthy, owner)



number = float(input("Enter the first number: "))
str_number = str(number)

type(str_number)