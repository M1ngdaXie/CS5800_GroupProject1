"""
GROUP 6 - DIVIDE AND CONQUER : TOP K MOST FREQUENT ELEMENTS
GEORGE LIN, MINDA XIE, ANDREW LI, XIAOTI HU
06-20-2025
"""

from typing import List
import heapq


class Solution1:
    """Sort-based solution with O(n log n) time complexity"""

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count frequency of each number
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # Sort by frequency and return top k elements
        sorted_items = sorted(count.items(), key=lambda item: item[1], reverse=True)
        return [item[0] for item in sorted_items[:k]]


class Solution2:
    """Bucket sort solution with O(n) time complexity"""

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count frequency of each number
        count = {}
        # Create buckets for each possible frequency (0 to n)
        freq = [[] for i in range(len(nums) + 1)]
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # Place numbers in their frequency buckets
        for n, c in count.items():
            freq[c].append(n)

        # Collect numbers from highest frequency buckets
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        return res


class Solution3:
    """Heap-based solution with O(n log k) time complexity"""

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count frequency of each number
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # Use min heap to efficiently get top k elements
        # heapq.nlargest automatically handles the heap operations
        return heapq.nlargest(k, count.keys(), key=lambda x: count[x])


def main():
    # main function used to test implementations
    # Initialize solution instances
    sol1 = Solution1()
    sol2 = Solution2()
    sol3 = Solution3()

    # Test Case 1: Basic case
    basic_case = [1, 1, 1, 2, 2, 3]
    k1 = 2

    results_match1 = (
        set(sol1.topKFrequent(basic_case, k1))
        == set(sol2.topKFrequent(basic_case, k1))
        == set(sol3.topKFrequent(basic_case, k1))
    )

    # Test Case 2: Single element
    single_case = [1]
    k2 = 1

    results_match2 = (
        set(sol1.topKFrequent(single_case, k2))
        == set(sol2.topKFrequent(single_case, k2))
        == set(sol3.topKFrequent(single_case, k2))
    )

    # Test Case 3: Larger dataset with negative numbers
    complex_case = [4, 1, -1, 2, -1, 2, 3, 4, 4, 4]
    k3 = 2

    results_match3 = (
        set(sol1.topKFrequent(complex_case, k3))
        == set(sol2.topKFrequent(complex_case, k3))
        == set(sol3.topKFrequent(complex_case, k3))
    )

    # Print results
    print(f"Test 1 - Basic case {basic_case}, k={k1}: {results_match1}")
    print(f"Test 2 - Single element {single_case}, k={k2}: {results_match2}")
    print(f"Test 3 - Complex case {complex_case}, k={k3}: {results_match3}")

    print("-" * 50)
    if results_match1 and results_match2 and results_match3:
        print("✅ ALL TESTS PASSED! All solutions return equivalent results.")


if __name__ == "__main__":
    main()
