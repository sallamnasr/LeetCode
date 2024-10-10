from typing import List
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        idx = [x for x in range(len(nums))]
        idx.sort(key=lambda x:nums[x])
        res  = 0 
        minIdx = len(nums)
        for num in idx :
            minIdx = min(num,minIdx)
            res = max(res,num-minIdx)
        return res 
x = Solution()
print(x.maxWidthRamp([4,2,3,1]))