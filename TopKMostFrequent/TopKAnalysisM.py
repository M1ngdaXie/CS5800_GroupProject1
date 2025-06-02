import time
import matplotlib.pyplot as plt
import heapq
from typing import List
import random
import sys
from TopKBasic import Solution1
from TopKBucketSort import Solution2
from TopKHeap import Solution3


def generate_test_data(size, unique_ratio):
    """Generate test data with controlled number of unique elements"""
    unique_count = max(1, int(size * unique_ratio))
    data = []
    for i in range(unique_count):
        frequency = random.randint(1, size // unique_count + 10)
        data.extend([i] * frequency)
    random.shuffle(data)
    return data[:size]


# Input sizes for testing
input_sizes = [100, 500, 1000, 5000, 10000, 20000]

# Check for command line argument
if len(sys.argv) > 1:
    # Single ratio mode
    ratio_choice = int(sys.argv[1])
    ratios = {1: 0.1, 2: 0.5, 3: 0.9}
    unique_ratio = ratios.get(ratio_choice, 0.1)
    scenario_names = {1: "Low (10%)", 2: "Medium (50%)", 3: "High (90%)"}
    scenario = scenario_names.get(ratio_choice, "Low (10%)")

    print(f"Testing with {scenario} unique ratio ({unique_ratio})")

    times1, times2, times3 = [], [], []
    for size in input_sizes:
        test_data = generate_test_data(size, unique_ratio)
        k = 10

        start = time.perf_counter()
        Solution1().topKFrequent(test_data, k)
        times1.append(time.perf_counter() - start)

        start = time.perf_counter()
        Solution2().topKFrequent(test_data, k)
        times2.append(time.perf_counter() - start)

        start = time.perf_counter()
        Solution3().topKFrequent(test_data, k)
        times3.append(time.perf_counter() - start)

    plt.figure(figsize=(10, 6))
    plt.plot(input_sizes, times1, label="Sort-based (O(n log n))", marker="o")
    plt.plot(input_sizes, times2, label="Bucket Sort (O(n))", marker="o")
    plt.plot(input_sizes, times3, label="Heap-based (O(n log k))", marker="o")
    plt.xlabel("Input Size (n)")
    plt.ylabel("Execution Time (seconds)")
    plt.title(f"Top K Frequent Elements: Timing Analysis - {scenario} Unique Ratio")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

else:
    # Default: run all ratios and show three plots
    scenarios = [(0.1, "Low (10%)"), (0.5, "Medium (50%)"), (0.9, "High (90%)")]

    fig, axes = plt.subplots(1, 3, figsize=(18, 6))

    for idx, (unique_ratio, scenario) in enumerate(scenarios):
        print(f"Testing {scenario} unique ratio...")

        times1, times2, times3 = [], [], []
        for size in input_sizes:
            test_data = generate_test_data(size, unique_ratio)
            k = 10

            start = time.perf_counter()
            Solution1().topKFrequent(test_data, k)
            times1.append(time.perf_counter() - start)

            start = time.perf_counter()
            Solution2().topKFrequent(test_data, k)
            times2.append(time.perf_counter() - start)

            start = time.perf_counter()
            Solution3().topKFrequent(test_data, k)
            times3.append(time.perf_counter() - start)

        ax = axes[idx]
        ax.plot(input_sizes, times1, label="Sort-based (O(n log n))", marker="o")
        ax.plot(input_sizes, times2, label="Bucket Sort (O(n))", marker="o")
        ax.plot(input_sizes, times3, label="Heap-based (O(n log k))", marker="o")
        ax.set_xlabel("Input Size (n)")
        ax.set_ylabel("Execution Time (seconds)")
        ax.set_title(f"{scenario} Unique Ratio")
        ax.legend()
        ax.grid(True)

    plt.tight_layout()
    plt.show()
