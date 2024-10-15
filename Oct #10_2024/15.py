class Solution:
    def minimumSteps(self, s: str) -> int:
        black,swap = 0,0 
        for ch in s :
            if ch == '0' :
                swap += black 
            else :
                black += 1 
        return swap 


x = Solution()
print(x.minimumSteps("0111"))
