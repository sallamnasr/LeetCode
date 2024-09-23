from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        lst = list(str(x) for x in range(1, n+1))
        lst.sort(key=lambda x: x)
        lst = [int(x) for x in lst]
        return lst


x = Solution()
print(x.lexicalOrder(13))
