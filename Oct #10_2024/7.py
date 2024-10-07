class Solution:
    def minLength(self, s: str) -> int:

        while True:
            if 'AB' in s:
                s = s.replace('AB', '')
            if 'CD' in s:
                s = s.replace('CD', '')
            if ('CD' not in s) and ('AB' not in s):
                return len(s)


x = Solution()
print(x.minLength('ACBBD'))
