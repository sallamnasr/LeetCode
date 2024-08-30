# Binary Search 
# time : O(log(n))
from typing import List
class Solution:
    def find_pivot(self, arr: List[int]):
        l = 0
        r = len(arr) - 1
        while l <= r:
            mid = l + (r-l)//2
            if arr[mid] > arr[-1]:
                l = mid + 1
            else:
                r = mid - 1
        return l

    def search(self, nums: List[int], target: int) -> int:
        end_start = self.find_pivot(nums)
        nums1 = nums[:end_start]
        nums2 = nums[end_start:]

        l, r = 0, len(nums1) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums1[mid] == target:
                return mid
            elif nums1[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        l, r = 0, len(nums2) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums2[mid] == target:
                return mid + end_start
            elif nums2[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return -1
