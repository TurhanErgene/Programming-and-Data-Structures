import matplotlib.pyplot as plt
import time
from list_gen import generate_random_integers  # Assume the utility function is available

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
                if nums[i] + nums[j] + nums[k] == 0:
                    result.add(tuple(sorted((nums[i], nums[j], nums[k]))))  # Sort to ensure uniqueness

    return list(result)

# Measure Performance with Averaging
def measure_time(repeats=3, sizes=range(100, 1101, 50)):
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

# Visualize Performance with Multiple Runs
def visualize_performance():
    """
    Plots performance data for three separate runs and their averages.
    """
    sizes = range(100, 1101, 50)
    all_times = []

    # Collect times for three separate runs
    for _ in range(3):
        _, times = measure_time(repeats=1, sizes=sizes)  # Each run is measured once
        all_times.append(times)

    # Plot three separate runs as points
    plt.figure(figsize=(10, 5))
    for i, run_times in enumerate(all_times, 1):
        plt.scatter(sizes, run_times, label=f'Run {i}', s=50)  # Scatter plot for individual runs

    # Compute average times for all runs
    avg_times = [sum(run[i] for run in all_times) / len(all_times) for i in range(len(sizes))]
    plt.scatter(sizes, avg_times, color='black', label='Average', s=60, marker='s')  # Scatter plot for averages

    plt.title('3-Sum Brute Force Performance (Multiple Runs)')
    plt.xlabel('Input Array Size')
    plt.ylabel('Execution Time (seconds)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Log-Log Plot and Linear Regression
def log_log_analysis():
    """
    Performs log-log analysis and plots with a straight-line fit.
    """
    import math  # Moved import here to avoid unused imports
    sizes, times = measure_time(repeats=3, sizes=range(100, 1101, 200))
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
    plt.plot(log_sizes, log_times, 'o', label='Log-Log Data')
    # plt.plot(log_sizes, [k * x + b for x in log_sizes], 'r-', label=f'Fit (k={k:.2f})')
    plt.title('Log-Log Plot and Linear Regression')
    plt.xlabel('log(Input Array Size)')
    plt.ylabel('log(Execution Time)')
    plt.legend()
    plt.grid(True)
    plt.show()

    print(f"Time Complexity Coefficient (k): {k:.2f}")

# Main
if __name__ == "__main__":
    # Visualize separate runs and their averages
    visualize_performance()

    # Perform log-log analysis
    log_log_analysis()
