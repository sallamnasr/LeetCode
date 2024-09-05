# 2028. Find Missing Observations ---->>> Medium.....
from typing import List
class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        total_sum = mean*(n+m) 
        curr_sum = sum(rolls)
        miss_sum = total_sum - curr_sum 
        if miss_sum < n or miss_sum > 6*n :
            return []
        val = miss_sum//n
        remain = miss_sum % n
        res = [val for _ in range(n)]
        for i in range(remain) :
            res[i] += 1
        return res 
        