
# this solution give time limit in 171 from 177 tests 
from typing import List
def firstMissingPositive(nums): 
    mini = 1
    for i in nums :
        if i>0 :
            mini = min(mini,i)
    if mini not in nums :
        return mini
    largg = max(nums) 
    for i in range(mini,largg+2) :
        if i not in nums :
            return i
    

# this sol give acc and this sol from chat gpt


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
            
        return n + 1
