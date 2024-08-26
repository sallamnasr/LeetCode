from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = float('inf')
        nums.sort()
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                curr = nums[i] + nums[l] + nums[r]
                if abs(target - curr) < abs(ans - target):
                    ans = curr
                if curr < target:
                    l += 1
                else:
                    r -= 1
        return ans

