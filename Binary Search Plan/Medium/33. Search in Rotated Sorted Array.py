# Binary Search 
# time : O(log(n))


from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def min_idx(arr):
            l, r = 0, len(arr) - 1
            while l < r:
                mid = l + (r-l)//2
                if arr[mid] > arr[r]:
                    l = mid + 1
                else:
                    r = mid
            return l
        pivot = min_idx(nums)
        l, r = 0, pivot - 1
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        l, r = pivot, len(nums) - 1
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1


x = Solution()
print(x.search([4, 5,6,7,0,1,2],0))