import random
import time
import matplotlib.pyplot as plt
from sort_algorithms import selection_sort, bubble_sort, insertion_sort

# Function to evaluate performance
def evaluate_algorithms(algorithms, sizes):
    timings = {name: [] for name in algorithms}

    for size in sizes:
        arr = random.sample(range(size * 10), size)  # Generate random data

        for name, algo in algorithms.items():
            start_time = time.time()
            algo(arr)  # Call the sorting function
            elapsed_time = time.time() - start_time
            timings[name].append(elapsed_time)

    return timings

# Plot the results with two subplots
def plot_timings(timings, sizes):
    fig, axes = plt.subplots(1, 2, figsize=(15, 5))

    # Subplot 1: Running times
    for name, timing in timings.items():
        axes[0].plot(sizes, timing, marker='x' if name == "Insertion Sort" else '+', linestyle='None', label=name)
    axes[0].set_xlabel('List sizes in range 2000 to 10000')
    axes[0].set_ylabel('Average time of 3 runs (seconds)')
    axes[0].set_title('Running times for O(n^2) algorithms')
    axes[0].legend()

    # Subplot 2: Log-log plot
    for name, timing in timings.items():
        log_sizes = [size for size in sizes]
        log_timings = [time for time in timing]
        axes[1].loglog(log_sizes, log_timings, marker='x' if name == "Insertion Sort" else '+', linestyle='None', label=name)
    axes[1].set_xlabel('Log2 of list sizes')
    axes[1].set_ylabel('Log2 of sorting times')
    axes[1].set_title('Log-log plots for O(n^2) algorithms')
    axes[1].legend()

    plt.tight_layout()
    plt.show()

# Define sorting algorithms
algorithms = {
    "Selection Sort": selection_sort,
    "Bubble Sort": bubble_sort,
    "Insertion Sort": insertion_sort
}

# Define input sizes
sizes = range(2000, 10001, 1000)  # Larger sizes for O(n^2)

# Evaluate and plot
timings = evaluate_algorithms(algorithms, sizes)
plot_timings(timings, sizes)
