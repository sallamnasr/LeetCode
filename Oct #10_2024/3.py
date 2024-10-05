from typing import List
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        TotalSum = sum(nums)
        remainder = TotalSum % p 
        if remainder == 0 :
            return 0 
        prefixsum = 0 
        prefixmod = {0:-1}
        ans = len(nums)
        
        for idx,num in enumerate(nums) :
            prefixsum += num 
            curr = prefixsum % p
            targetMod = (curr - remainder + p) % p

            if targetMod in prefixmod :
                ans = min(ans,idx-prefixmod[targetMod])
            prefixmod[curr] = idx
        return ans if ans<len(nums) else -1 