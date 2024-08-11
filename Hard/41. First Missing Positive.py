from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = sorted([num for num in nums if num > 0])

        if not nums or nums[0] != 1:
            return 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1 and nums[i] != nums[i-1]:
                return nums[i-1] + 1

        return nums[-1] + 1
