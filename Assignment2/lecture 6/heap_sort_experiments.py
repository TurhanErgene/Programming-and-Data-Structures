from Heap import Heap
from sort_algorithms import quick_sort, merge_sort
import random
import time
import matplotlib.pyplot as plt

# Heap Sort Implementation
def heap_sort(arr):
    heap = Heap()
    for elem in arr:
        heap.add(elem)

    # Extract elements in sorted order
    sorted_arr = []
    while not heap.is_empty():
        sorted_arr.append(heap.pull_high())

    return sorted_arr[::-1]  # Return in ascending order

# Helper function to evaluate sorting algorithms
def evaluate_sorting_algorithms():
    sizes = [100, 500, 1000, 5000, 10000]
    algorithms = {"Heap Sort": heap_sort, "Quick Sort": quick_sort, "Merge Sort": merge_sort}
    results = {name: [] for name in algorithms}

    for size in sizes:
        for name, algorithm in algorithms.items():
            total_time = 0
            for _ in range(5):  # Average of 5 runs
                arr = [random.randint(1, 100000) for _ in range(size)]
                start_time = time.time()
                algorithm(arr)
                total_time += time.time() - start_time
            avg_time = total_time / 5
            results[name].append(avg_time)

    # Plot results
    for name, times in results.items():
        plt.plot(sizes, times, label=name)
    plt.xlabel("Input Size")
    plt.ylabel("Average Time (s)")
    plt.title("Comparison of Sorting Algorithms")
    plt.legend()
    plt.show()

# Run the evaluation
evaluate_sorting_algorithms()
