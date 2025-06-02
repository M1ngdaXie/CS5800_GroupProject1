import time
import matplotlib.pyplot as plt
import heapq
from typing import List
import random
from TopKBasic import Solution1
from TopKBucketSort import Solution2
from TopKHeap import Solution3


# Input sizes for testing
input_sizes = [100, 500, 1000, 5000, 10000, 20000]
times1, times2, times3 = [], [], []

# Time each algorithm on the input sizes
for size in input_sizes:
    test_data = [random.randint(0, size // 10) for _ in range(size)]
    k = 10

    # Solution 1
    start = time.perf_counter()
    Solution1().topKFrequent(test_data, k)
    times1.append(time.perf_counter() - start)

    # Solution 2
    start = time.perf_counter()
    Solution2().topKFrequent(test_data, k)
    times2.append(time.perf_counter() - start)

    # Solution 3
    start = time.perf_counter()
    Solution3().topKFrequent(test_data, k)
    times3.append(time.perf_counter() - start)


plt.figure(figsize=(10, 6))
plt.plot(input_sizes, times1, label="Sort-based (O(n log n))", marker="o")
plt.plot(input_sizes, times2, label="Bucket Sort (O(n))", marker="o")
plt.plot(input_sizes, times3, label="Heap-based (O(n log k))", marker="o")
plt.xlabel("Input Size (n)")
plt.ylabel("Execution Time (seconds)")
plt.title("Top K Frequent Elements: Timing Analysis")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
