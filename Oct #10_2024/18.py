from typing import List

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        mxOR = 0 
        for num in nums :
            mxOR |= num 

        def backtrack(i, current_or):
            if i == len(nums):
                return 1 if current_or == mxOR else 0

            include = backtrack(i + 1, current_or | nums[i])  
            exclude = backtrack(i + 1, current_or)            

            return include + exclude
        return backtrack(0,0)

# x = Solution()
# print(x.countMaxOrSubsets())