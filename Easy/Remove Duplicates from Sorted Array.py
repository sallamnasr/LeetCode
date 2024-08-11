from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            else:
                idx += 1
                nums[idx] = nums[i]
        return idx + 1
if __name__ == "__main__" :
    pass