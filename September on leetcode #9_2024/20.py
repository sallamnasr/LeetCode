class Solution:
    def IsPalindrom(self, s: str) -> bool:
        return s == s[::-1]

    def shortestPalindrome(self, s: str) -> str:
        
        curr = ''
        for i in range(len(s)-1,-1,-1) :
            curr += s[i] 
            if self.IsPalindrom(curr+s) :
                return curr + s