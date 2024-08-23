from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        idx = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                idx = i
                break

        rotated_nums = nums[idx:] + nums[:idx]

        l = 0
        r = len(rotated_nums) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if rotated_nums[mid] == target:
                return True
            elif rotated_nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return False

    
x = Solution()

print(x.search([2,5,6,0,0,1,2],3))