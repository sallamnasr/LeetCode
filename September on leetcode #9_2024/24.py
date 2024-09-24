from typing import List


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        mp = {}
        for x in arr1:
            x = str(x)
            prefix = ''
            for ch in x:
                prefix += ch
                if prefix not in mp:
                    mp[prefix] = 0
                mp[prefix] += 1

        mx = 0
        for y in arr2:
            y = str(y)
            prefix = ''
            for ch in y:
                prefix += ch
                if prefix in mp:
                    mx = max(len(prefix), mx)
                else:
                    break
        return mx


x = Solution()
print(x.longestCommonPrefix([123, 234, 345], [12, 23, 1234]))


x = Solution()
print(x.longestCommonPrefix([1, 2, 3],[4,4,4,4]))
