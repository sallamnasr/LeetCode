from collections import deque
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        cnt = 0 
        stk = deque()
        for ch in s :
            if ch == '(' :
                stk.append(ch)
            else :
                if not stk :
                    cnt += 1 
                else :
                    stk.pop()
        return cnt + len(stk)
        


x = Solution()
print(x.minAddToMakeValid("((("))
