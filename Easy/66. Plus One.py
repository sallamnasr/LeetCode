from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ''
        for x in digits:
            num += str(x)
        num = int(num) + 1
        num = str(num)
        res = []
        for i in num:
            res.append(i)
        return res


x = Solution()

print(x.plusOne([9,9]))
