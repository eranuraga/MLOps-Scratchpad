#Exercise N1 — List vs NumPy
numbers = [1, 2, 3, 4]
print(numbers * 2)
#[1, 2, 3, 4, 1, 2, 3, 4]

import numpy_practice as np

numbers = np.array([1, 2, 3, 4])
print(numbers * 2)
# [2 4 6 8]


#Exercise N2
cpu = np.array([82, 55, 91, 67])
print(type(cpu))
print(cpu.shape)
print(cpu.size)
print(cpu.ndim)

#Exercise N3
metrics = np.array([
    [82, 71],
    [55, 60],
    [91, 84]
])

#CPU of payment-api
print(metrics[0,0])
#Memory of payment-api
print(metrics[0,1])
#CPU of inventory-api
print(metrics[2,0])
#Entire second row
print(metrics[1,])
#Entire first column
print(metrics[:, 0])
#First two rows
print(metrics[0:2, :])

#Vectorized Operations Exercise N4
latencies = np.array([
    120,
    340,
    89,
    450,
    230
])
print(latencies + 10)
print(latencies * 2)
print(latencies / 100)
print(latencies > 300)

#Boolean Masking
latencies = np.array([
    120,
    340,
    89,
    450,
    230
])
print(latencies[latencies > 300])

#Exercise N5 — SRE Filtering
latencies = np.array([
    120, 450, 80, 600, 210, 90, 510
])
#requests > 300 ms
print(latencies[latencies > 300])
#requests < 100 ms
print(latencies[latencies < 100])
#requests between 100 and 300 ms
# Create the boolean mask
mask = (latencies >= 100) & (latencies <= 300)

# Apply the mask to filter the array
filtered_latencies = latencies[mask]

print(filtered_latencies)
# Output: [120 210]

#Aggregation
latencies = np.array([
    120, 450, 80, 600, 210, 90, 510
])
print(np.sum(latencies))
print(np.average(latencies))
print(np.min(latencies))
print(np.max(latencies))
print(np.std(latencies))

# Axis
metrics = np.array([
    [82, 71],
    [55, 60],
    [91, 84]
])

print(np.mean(metrics))
print(np.mean(metrics, axis=0))
print(np.mean(metrics, axis=1))

# Exercise N6
metrics = np.array([
    [82, 71],
    [55, 60],
    [91, 84]
])

print(np.mean(metrics, axis=0))
print(np.mean(metrics))
print(np.mean(metrics, axis=1))

np.zeros(5)
np.ones(5)
np.arange(0, 10, 2)
np.linspace(0, 1, 5)

##Exercise N7
data = np.arange(24)
print(data.reshape(6,4))
print(data.reshape(6,4).shape)
print(data.reshape(6,4).size)
print(data.reshape(4,6))
print(data.reshape(4,6).shape)
print(data.reshape(4,6).size)

## Numpy challenge
metrics = np.array([
    [82, 71, 0.02],
    [55, 60, 0.01],
    [91, 84, 0.07],
    [67, 52, 0.03],
    [88, 79, 0.06]
])
np.ndim(metrics)
print(f"Shape of metrics: {np.shape(metrics)}")
print(f"Average of CPU: {np.average(metrics[:, 0])}")
print(f"Average of Memory: {np.average(metrics[:, 1])}")
print(f"Highest CPU: {np.max(metrics[:, 0])}")
print(f"Highest Error Rate: {np.max(metrics[:, 2])}")
print(f"Services CPUs higher than 80: {metrics[metrics[:, 0] > 80, 0 ]}")
print(f"Services error rate higher than 0.05: {metrics[metrics[:, 2] > 0.05, 2]}")
print(f"Average metrics across services: {np.mean(metrics)}")
print(f"Normalize CPU to a 0–1 scale by dividing by 100: {metrics[:,0] / 100}")
reshaped = metrics.reshape(3, 5)
print(f"Reshape the array into a valid new shape and explain what changed: {reshaped}")