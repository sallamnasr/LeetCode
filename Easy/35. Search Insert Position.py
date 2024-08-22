from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums) - 1
        if target > nums[r] :
            return r+1
        elif target <= nums[l] :
            return l
        
        while l<=r :
            mid = l + (r-l)//2 
            if nums[mid] == target :
                return mid 
            
            elif nums[r] == target :
                return r 
            
            elif nums[l] == target :
                return l 
            
            elif nums[mid] > target :
                r = mid
            
            elif nums[mid] < target :
                l = mid 
                
            if r-l == 1 :
                if target > nums[l] and target < nums[r] :
                    return l + 1 
                elif target == nums[l] :
                    return l 
                else :
                    return r 
                
# x = Solution() 

# print(x.searchInsert([1,3,5,6],7))