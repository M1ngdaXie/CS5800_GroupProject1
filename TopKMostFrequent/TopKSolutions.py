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
