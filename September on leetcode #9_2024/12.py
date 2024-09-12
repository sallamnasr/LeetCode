from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        cnt = 0
        for word in words:
            flag = True
            for ch in word:
                if ch not in allowed:
                    flag = False
            if flag == True:
                cnt += 1
        return cnt


x = Solution()
print(x.countConsistentStrings(
    'cad', ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]))
