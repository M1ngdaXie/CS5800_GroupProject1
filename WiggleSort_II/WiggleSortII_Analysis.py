"""
GROUP 6 - DIVIDE AND CONQUER : TOP K MOST FREQUENT ELEMENTS
GEORGE LIN, MINDA XIE, ANDREW LI, XIAOTI HU
06-17-2025
"""
import argparse
import time
import random
import matplotlib.pyplot as plt

from Brute_Force import wiggleSort as wiggleSort_brute
from Divide_and_Conquer import wiggleSort as wiggleSort_divide
from Greedy import wiggleSort as wiggleSort_greedy

# check if the array is wiggle sorted
# A wiggle sorted array has the property that nums[0] < nums[1], ums[1] > nums[2], nums[2] < nums[3]
# and so on, alternating between less than and greater than.
# This function checks if the input array satisfies this property.
# It returns True if the array is wiggle sorted, otherwise False.
def is_wiggle_sorted(nums):
    for i in range(len(nums)-1):
        if i % 2 == 0 and nums[i] > nums[i+1]:
            return False
        if i % 2 == 1 and nums[i] < nums[i+1]:
            return False
    return True

# Benchmarking function to measure execution time of wiggle sort algorithms
# It takes a function, a list of input sizes, and a unique ratio.
# It generates random arrays based on the input sizes and unique ratio,
# runs the wiggle sort function on each array, and measures the time taken.
# It returns a list of execution times for each input size.
def benchmark(func, input_sizes, unique_ratio):
    times = []
    for size in input_sizes:
        unique_count = max(size // 2, int(size * unique_ratio))
        base = list(range(unique_count))
        arr = [random.choice(base) for _ in range(size)]
        start = time.perf_counter()
        result = func(arr[:])
        end = time.perf_counter()
        if not is_wiggle_sorted(result):
            raise ValueError(f"{func.__name__} failed wiggle sort property for size {size}")
        times.append(end - start)
    return times

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Benchmark wiggle sort algorithms")
    parser.add_argument('--ratios', type=float, nargs='+', default=[0.1, 0.5, 0.9],
                        help='Uniqueness ratios (e.g. 0.1 0.5 0.9)')
    parser.add_argument('--sizes', type=int, nargs='+', default=[1000, 5000, 10000],
                        help='Input sizes (e.g. 1000 5000 10000)')
    args = parser.parse_args()

    # Ensure ratios are valid
    if any(r < 0 or r > 1 for r in args.ratios):
        raise ValueError("Ratios must be between 0 and 1.")
    if any(size <= 0 for size in args.sizes):
        raise ValueError("Input sizes must be positive integers.")
    input_sizes = args.sizes
    ratios = args.ratios

    # Prepare titles for plots
    titles = [f"Unique {int(r * 100)}%" for r in ratios]

    fig, axes = plt.subplots(1, len(ratios), figsize=(6 * len(ratios), 5), sharey=True)

    if len(ratios) == 1:
        axes = [axes]  # Ensure iterable

    # Benchmark each algorithm for each ratio
    print("Starting benchmarks...")
    for idx, ratio in enumerate(ratios):
        brute_times = benchmark(wiggleSort_brute, input_sizes, ratio)
        divide_times = benchmark(wiggleSort_divide, input_sizes, ratio)
        greedy_times = benchmark(wiggleSort_greedy, input_sizes, ratio)

        ax = axes[idx]
        ax.plot(input_sizes, brute_times, marker='o', label='Brute-force (O(n log n))')
        ax.plot(input_sizes, divide_times, marker='o', label='Divide & Conquer (O(n))')
        ax.plot(input_sizes, greedy_times, marker='o', label='Greedy (O(n log n))')

        ax.set_title(titles[idx])
        ax.set_xlabel('Input Size (n)')
        ax.set_ylabel('Execution Time (seconds)')
        ax.grid(True)
        ax.legend()

    plt.tight_layout()
    plt.savefig("wiggleSort_Result_RealTime.png", dpi=200)
    plt.show()

if __name__ == "__main__":
    main()
