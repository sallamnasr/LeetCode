class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        res = ''
        for i in range(len(s)-1, -1, -1):
            res += s[i] + ' '
        return res


x = Solution()
print(x.reverseWords('nasr r sallam'))
