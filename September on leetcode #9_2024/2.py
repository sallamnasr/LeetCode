# Find the Student that Will Replace the Chalk -> Medium
from typing import List
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        sm = sum(chalk)
        k = k % sm
        i = 0
        while chalk[i] <= k:
            k -= chalk[i]
            i += 1
        return i


# x = Solution()
# print(x.chalkReplacer([3,4,1,2],25))