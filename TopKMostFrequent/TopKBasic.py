from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        sorted_items = sorted(count.items(), key=lambda item: item[1], reverse=True)
        return [item[0] for item in sorted_items[:k]]


solution = Solution()
print(solution.topKFrequent([1, 1, 1, 2, 2, 3], 2))
print(solution.topKFrequent([1], 1))
