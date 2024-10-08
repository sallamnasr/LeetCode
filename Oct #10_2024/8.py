class Solution:
    def minSwaps(self, s: str) -> int:
        cnt = 0 
        for ch in s :
            if ch == '[' :
                cnt += 1 
            if ch == ']' and cnt > 0 :
                cnt -= 1
        return (cnt+1) //2