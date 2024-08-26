from typing import List
class Solution:
    
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l += 1
            else:
                r -= 1
        return -1



# Link for problem :
#     https://leetcode.com/problems/binary-search/?envType =study-plan-v2&envId=binary-search