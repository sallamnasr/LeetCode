# with two pointer Method
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1

        while l <= r:
            sum = target * 2
            if sum == nums[l] + nums[r] and nums[l] == target and nums[r] == target:
                return [l, r]
            elif sum > nums[l] + nums[r]:
                l += 1
            else:
                r -= 1
        return [-1, -1]

# with binary search Method 

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1
        x = 0
        while l < r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                x = mid
                break
            elif nums[mid] < target:
                l = mid
            elif nums[mid] > target:
                r = mid

            if r-l == 1 and nums[l] != target and nums[r] != target:
                break
            elif r-l == 1 and (nums[l] == target or nums[r] != target):
                break
            else:
                break

        while l <= r:
            if nums[l] == target:
                break
            l += 1
        while l <= r:
            if nums[r] == target:
                break
            r -= 1

        if l <= r:
            return [l, r]
        else:
            return [-1, -1]


# x = Solution()

# print(x.searchRange([1, 4], 4))
