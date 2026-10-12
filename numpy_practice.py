import numpy as np

numbers = [1,2,3,4,5]
print(numbers * 2)

for number in numbers:
    print(number * 2)

latencies = np.array([120,240,89,450,230])
print(latencies + 10)
print(latencies * 2)
print(latencies / 100)
print(type(latencies))

print(latencies.size)
print(latencies.shape)
print(latencies.ndim)
print(latencies.dtype)

print(latencies[:2])
print(latencies[2:])
print(latencies[:])

metrics = np.array([
    [82, 71],
    [55, 60],
    [91, 84]
])

print(metrics.shape)
print(metrics.size)
print(metrics.ndim)

print(metrics[0,0])
print(metrics[0,1])
print(metrics[1,0])
print(metrics[2,1])

print(metrics[0,:])
print(metrics[:,1])


#SRE dataset

metrics = np.array([
    [82, 71, 120],
    [55, 60, 340],
    [91, 84, 450],
    [67, 52, 180],
    [88, 79, 510]
])

print(metrics[:, 0])
print(metrics[:, 1])
print(metrics[:, 2])
print(metrics[:,0:2])

cpu = metrics[:,0]
print(cpu/100)
print(f"Normalized Memory: {metrics[:,1]/100}")
print(f"Adding 10ms to latency: {metrics[:,2] + 10}")

print(metrics.shape)
print(metrics.size)
print(metrics.ndim)
print(metrics.dtype)

print(metrics[:, 0])
print(metrics[:, 1])
print(metrics[:, 2])

print(metrics[0,:])
print(metrics[2,:])
print(metrics[-1,:])
print(metrics[0:3,:])

print(metrics[:, 0:2])
print(metrics[:, 1:3])

print(metrics[:, 0] / 100)
print(metrics[:, 1] / 100)
print(metrics[:, 2] / 1000)
print(metrics[:, 2] + 0.1)

## NumPy Day2
latencies = np.array([
    120,
    450,
    80,
    600,
    210,
    90,
    510
])

print(latencies > 300)
print(latencies[latencies > 300])

print(metrics[metrics[:,0] > 80])
print(metrics[metrics[:,1] > 70])
print(metrics[metrics[:, 2] > 300])
print(metrics[(metrics[:,0] > 80) & (metrics[:,2] > 300)])
print(metrics[(metrics[:,0] > 80) | (metrics[:, 1] > 80)])

print(np.sum(latencies))
print(np.min(latencies))
print(np.max(latencies))
print(np.mean(latencies))

print(np.mean(metrics, axis=1))

print(np.sum(metrics[:,0] > 80))

data = np.arange(24)
print(data.reshape(4,6))
data.reshape(
    6,
    -1
)


## Final NumPy Challenge
metrics = np.array([
    [82, 71, 120],
    [55, 60, 340],
    [91, 84, 450],
    [67, 52, 180],
    [88, 79, 510]
])

print(metrics[metrics[:,0] > 80])
print(metrics[metrics[:,2] > 300])
print(metrics[(metrics[:, 0] > 80) & (metrics[:,2] > 300)])
print(metrics[(metrics[:,1] > 70) | (metrics[:,2] > 400)])

print(np.mean(metrics[:,0]))
print(np.mean(metrics[:,1]))
print(np.mean(metrics[:,2]))
print(np.max(metrics[:,0]))
print(np.min(metrics[:,2]))
print(np.std(metrics[:,2]))

np.mean(metrics, axis=0)
np.max(metrics, axis=0)

print(np.sum(metrics[:,0] > 80))
print(np.mean(metrics[:,0] > 80))
print(np.sum(metrics[:,2] > 300))
print(np.mean(metrics[:,2] > 300))



How many samples? 5
How many features? 3
What does one row represent? sample containing normalized cpu, memory and latency
What does one column represent? feature
What is X.shape? (5,3)

Why must len(y) correspond to the number of rows in X? because the targets should corresponds to each sample (ie each row)