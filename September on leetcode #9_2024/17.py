from typing import List
from collections import defaultdict


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:

        s = s1 + ' ' + s2
        dc = defaultdict(int)
        for word in s.split():
            dc[word] += 1

        result = []

        for key, val in dc.items():
            if val == 1:
                result.append(key)
        return result


x = Solution()
print(x.uncommonFromSentences("apple apple", "banana"))
