
from typing import List


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:

        mp = {}
        for word in words:
            prefix = ''
            for ch in word:
                prefix += ch
                if prefix not in mp:
                    mp[prefix] = 0
                mp[prefix] += 1
        result = []
        for word in words:
            prefix = ''
            cnt = 0
            for ch in word:
                prefix += ch
                cnt += mp[prefix]
            result.append(cnt)
        return result


x = Solution()
print(x.sumPrefixScores(["abcd"]))
