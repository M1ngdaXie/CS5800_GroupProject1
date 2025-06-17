"""
GROUP 6 - DIVIDE AND CONQUER : TOP K MOST FREQUENT ELEMENTS
GEORGE LIN, MINDA XIE, ANDREW LI, XIAOTI HU
06-20-2025
"""

import time
import matplotlib.pyplot as plt
import random
import sys
from TopKSolutions import Solution1, Solution2, Solution3


def generate_test_data(size, unique_ratio):
    """Generate test data with controlled number of unique elements.

    Args:
        size: Total number of elements in the test data
        unique_ratio: Proportion of unique elements (0-1)
    Returns:
        List of numbers with controlled uniqueness and random frequencies
    """
    # Calculate how many unique numbers we want based on the ratio
    # Ensure at least one unique element
    unique_count = max(1, int(size * unique_ratio))
    data = []

    # For each unique number, generate random frequency of occurrences
    # Higher frequency means more duplicates of that number
    for i in range(unique_count):
        frequency = random.randint(1, size // unique_count + 10)
        data.extend([i] * frequency)

    # Shuffle to randomize the order of elements
    random.shuffle(data)
    return data[:size]


def parse_sizes(sizes_str):
    """Parse comma-separated sizes string into list of integers.

    Args:
        sizes_str: Comma-separated string of input sizes (e.g., "100,500,1000")
    Returns:
        List of integers representing input sizes
    """
    try:
        return [int(s.strip()) for s in sizes_str.split(",")]
    except ValueError:
        print(
            "Error: Invalid sizes format. Use comma-separated integers (e.g., '100,500,1000')"
        )
        sys.exit(1)


def print_usage():
    """Display help message explaining command line arguments and exit program."""
    print("Usage: python TopKAnalysisEnhanced.py [uniqueness_level] [sizes] [k]")
    print("  uniqueness_level: 1 (10%), 2 (50%), or 3 (90%)")
    print("  sizes: comma-separated list of input sizes (optional)")
    print("  k: number of top frequent elements to find (optional, default: 100)")
    sys.exit(1)


def run_analysis(unique_ratio, scenario, input_sizes, k):
    """Run performance analysis for all three solutions.

    Args:
        unique_ratio: Proportion of unique elements in test data
        scenario: Description of the uniqueness level
        input_sizes: List of different input sizes to test
        k: Number of top frequent elements to find
    Returns:
        Dictionary containing execution times for each solution
    """
    # Store execution times for each solution (1: sort-based, 2: bucket sort, 3: heap-based)
    times = {1: [], 2: [], 3: []}
    solutions = [Solution1(), Solution2(), Solution3()]

    # Test each input size to measure performance scaling
    for size in input_sizes:
        test_data = generate_test_data(size, unique_ratio)
        # Ensure k doesn't exceed number of unique elements in the data
        effective_k = min(k, len(set(test_data)))

        # Time each solution's performance
        for i, solution in enumerate(solutions, 1):
            start = time.perf_counter()
            solution.topKFrequent(test_data, effective_k)
            times[i].append(time.perf_counter() - start)

    return times


def plot_results(input_sizes, times, scenario, k, ax=None):
    """Create performance comparison plot for the solutions.

    Args:
        input_sizes: List of input sizes tested
        times: Dictionary of execution times for each solution
        scenario: Description of the uniqueness level
        k: Number of top elements found
        ax: Optional matplotlib axis for subplot
    """
    # Labels for each solution with their time complexity
    labels = [
        "Sort-based (O(n log n))",
        "Bucket Sort (O(n))",
        "Heap-based (O(n log k))",
    ]

    # Create new figure if no axis provided (single plot)
    if ax is None:
        plt.figure(figsize=(12, 7))
        ax = plt.gca()

    # Plot results for each solution with markers and lines
    for i, label in enumerate(labels, 1):
        ax.plot(input_sizes, times[i], label=label, marker="o", linewidth=2)

    # Configure plot appearance for better readability
    ax.set_xlabel("Input Size (n)", fontsize=11)
    ax.set_ylabel("Execution Time (seconds)", fontsize=11)
    ax.set_title(f"{scenario} Unique Ratio\n(k = {k})", fontsize=12)
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)


# Default test parameters
default_input_sizes = [
    150,
    500,
    1000,
    5000,
    10000,
    20000,
]  # Range of input sizes to test
ratios = {
    1: (0.1, "Low (10%)"),
    2: (0.5, "Medium (50%)"),
    3: (0.9, "High (90%)"),
}  # Uniqueness levels

if __name__ == "__main__":
    # Handle help request (-h, --help, or help)
    if len(sys.argv) > 1 and sys.argv[1] in ["-h", "--help", "help"]:
        print_usage()

    try:
        # Parse command line arguments with defaults
        ratio_choice = int(sys.argv[1]) if len(sys.argv) > 1 else None
        input_sizes = (
            parse_sizes(sys.argv[2])
            if len(sys.argv) > 2 and sys.argv[2].lower() != "default"
            else default_input_sizes
        )
        k = int(sys.argv[3]) if len(sys.argv) > 3 else 100

        # Validate k value is positive
        if k <= 0:
            print("Error: k must be a positive integer")
            sys.exit(1)

        if ratio_choice is None:
            # Run and plot all scenarios (10%, 50%, 90% uniqueness)
            fig, axes = plt.subplots(1, 3, figsize=(20, 6))
            for idx, (ratio, scenario) in enumerate(ratios.values()):
                times = run_analysis(ratio, scenario, input_sizes, k)
                plot_results(input_sizes, times, scenario, k, axes[idx])
            plt.suptitle(
                "Top K Frequent Elements: Performance Comparison Across Uniqueness Ratios",
                fontsize=16,
                y=1.02,
            )
        else:
            # Run and plot single scenario based on user choice
            if ratio_choice not in ratios:
                print("Error: uniqueness_level must be 1, 2, or 3")
                print_usage()
            ratio, scenario = ratios[ratio_choice]
            times = run_analysis(ratio, scenario, input_sizes, k)
            plot_results(input_sizes, times, scenario, k)

        plt.tight_layout()
        plt.show()

    except ValueError:
        print("Error: Invalid input format")
        print_usage()
