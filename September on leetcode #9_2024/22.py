from typing import List


class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        lst = list(str(x) for x in range(1, n+1))
        lst.sort(key=lambda x: x)
        lst = [int(x) for x in lst]
        return lst[k-1]


x = Solution()
print(x.findKthNumber(13, 2))
