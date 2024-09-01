from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = l + (r-l)//2
            if nums[mid] > nums[r] :
                l = mid + 1 
            else :
                r = mid 
        
        return nums[l]


# time complixity is O(log(n))
# space complixity is O(1)