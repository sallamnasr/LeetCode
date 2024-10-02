from typing import List
from collections import Counter


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:

        remainder_count = Counter(x % k for x in arr)

        for r in range(k):
            if r == 0:
                if remainder_count[r] % 2 != 0:
                    return False
            else:
                if remainder_count[r] != remainder_count[k - r]:
                    return False

        return True


x = Solution()
print(x.canArrange([1, 2, 3, 4, 5, 10, 6, 7, 8, 9], k=5))
