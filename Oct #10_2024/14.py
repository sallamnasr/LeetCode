import heapq
from typing import List
import math


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)

        score = 0
        for _ in range(k):
            mx = -heapq.heappop(max_heap)
            score += mx
            heapq.heappush(max_heap, -math.ceil(mx / 3))

        return score


x = Solution()
print(x.maxKelements([1, 10, 3, 3, 3], k=3))
