class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur = ''
        mx = 0
        i, j = 0, 0
        while i < len(s):
            if s[i] not in cur:
                cur += s[i]
                i += 1
                mx = max(len(cur), mx)
            else:
                j += 1
                i = j
                cur = ''
        return mx
 
 
# the Complixity for this code  is O(n^2)
