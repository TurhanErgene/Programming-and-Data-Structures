import matplotlib.pyplot as plt
import time
from list_gen import generate_random_integers  


# Brute Force Solution for 3-Sum Problem
def three_sum_brute_force(nums):
    """
    Brute force solution to the 3-sum problem.
    Returns all unique triplets that sum to zero.
    """
    n = len(nums)
    result = set()

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:  # "0" is the sum
                    result.add(tuple(sorted((nums[i], nums[j], nums[k]))))  # Sort to ensure uniqueness

    return list(result)

# Measure Performance with Averaging
def measure_time(repeats=5, sizes=range(100, 1101, 50)):
    """
    Measures runtime of the brute force solution for given input sizes.
    Each data point is averaged over 'repeats' executions.
    """
    times = []

    for size in sizes:
        avg_time = 0
        for _ in range(repeats):
            nums = generate_random_integers(size=size, min_value=-10 * size, max_value=10 * size)
            start_time = time.time()
            three_sum_brute_force(nums)
            end_time = time.time()
            avg_time += (end_time - start_time)
        avg_time /= repeats
        times.append(avg_time)

    return list(sizes), times

# Visualize Separate Runs
def visualize_runs():
    """
    Plots performance data for three separate runs.
    """
    sizes = range(100, 1101, 50)
    all_times = []

    # Collect times for three separate runs
    for _ in range(3):
        _, times = measure_time(repeats=1, sizes=sizes)  # Each run is measured once
        all_times.append(times)

    markers = ["2","3","4"]

    # Plot three separate runs as points
    plt.figure(figsize=(10, 5))
    for i, (run_times, marker) in enumerate(zip(all_times, markers), 1):
        plt.scatter(sizes, run_times, label=f'Run {i}', s=50, marker=marker)  # Scatter plot for individual runs

    plt.title('3-Sum Brute Force Performance (Individual Runs)')
    plt.xlabel('Input Array Size')
    plt.ylabel('Execution Time (seconds)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Visualize Average Times
def visualize_average():
    """
    Plots the average execution time for multiple runs.
    """
    sizes, avg_times = measure_time(repeats=5, sizes=range(100, 1101, 50))

    plt.figure(figsize=(10, 5))
    plt.plot(sizes, avg_times, marker='o', label='Average Time', color='black', linestyle='--')
    plt.title('3-Sum Brute Force Performance (Average Time)')
    plt.xlabel('Input Array Size')
    plt.ylabel('Execution Time (seconds)')
    plt.legend()
    plt.grid(True)
    plt.show()


def log_log_analysis():
    """
    Performs log-log analysis and plots with a straight-line fit.
    """
    import math  # Moved import here to avoid unused imports
    sizes, times = measure_time(repeats=3, sizes=range(100, 1101, 50))
    log_sizes = [math.log(size) for size in sizes]
    log_times = [math.log(time) for time in times]

    # Linear regression
    n = len(log_sizes)
    sum_x = sum(log_sizes)
    sum_y = sum(log_times)
    sum_x2 = sum(x ** 2 for x in log_sizes)
    sum_xy = sum(x * y for x, y in zip(log_sizes, log_times))

    k = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
    b = (sum_y - k * sum_x) / n

    # Plot log-log data and regression line
    plt.figure(figsize=(10, 5))
    plt.plot(log_sizes, log_times, 'o', label='Log-Log Data')  # Blue points for log-log data
    plt.plot(log_sizes, [k * x + b for x in log_sizes], 'r-', label=f'Fit (y = {k:.2f}x + {b:.2f})')  # Red line for regression
    plt.title('Log-Log Plot and Linear Regression')
    plt.xlabel('log(Input Array Size)')
    plt.ylabel('log(Execution Time)')
    plt.legend()
    plt.grid(True)
    plt.show()

    print(f"Time Complexity Coefficient (k): {k:.2f}")

# log_log_analysis()

# visualize_runs()

visualize_average()
