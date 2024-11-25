import random
import time
import matplotlib.pyplot as plt
from sort_algorithms import merge_sort, quick_sort

# Function to evaluate performance
def evaluate_algorithms(algorithms, sizes):
    timings = {name: [] for name in algorithms}

    for size in sizes:
        for name, algo in algorithms.items():
            total_time = 0
            for _ in range(5):  # Average over 5 runs for accuracy
                arr = random.sample(range(size * 10), size)  # Generate random data
                start_time = time.time()
                algo(arr)  # Call the sorting function
                total_time += time.time() - start_time
            avg_time = total_time / 5
            timings[name].append(avg_time)

    return timings

# Plot the results
def plot_timings(timings, sizes):
    plt.figure(figsize=(8, 5))

    for name, timing in timings.items():
        plt.plot(sizes, timing, marker='+', linestyle='None', label=name)
    plt.xlabel('List sizes in range 10000 to 150000')
    plt.ylabel('Average time of 5 runs (seconds)')
    plt.title('Running times for n*log(n) algorithms')
    plt.legend()
    plt.show()

# Define sorting algorithms
nlogn_algorithms = {
    "Merge Sort": merge_sort,
    "Quick Sort": quick_sort
}

# Define input sizes
nlogn_sizes = range(10000, 150001, 10000)  # Sizes for O(n*log(n))

# Evaluate and plot
nlogn_timings = evaluate_algorithms(nlogn_algorithms, nlogn_sizes)
plot_timings(nlogn_timings, nlogn_sizes)
