from typing import List
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count frequencies
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # Use heapq to get top k elements
        return heapq.nlargest(k, count.keys(), key=lambda x: count[x])
