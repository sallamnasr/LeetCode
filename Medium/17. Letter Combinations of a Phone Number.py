from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        dc = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        ln = len(digits)
        if ln == 0:
            return []
        elif ln == 1:
            for i in dc[digits]:
                res.append(i)
        elif ln == 2:
            for i in dc[digits[0]]:
                for j in dc[digits[1]]:
                    res.append(i + j)
        elif ln == 3:
            for i in dc[digits[0]]:
                for j in dc[digits[1]]:
                    for k in dc[digits[2]]:
                        res.append(i + j + k)
        elif ln == 4:
            for i in dc[digits[0]]:
                for j in dc[digits[1]]:
                    for k in dc[digits[2]]:
                        for z in dc[digits[3]]:
                            res.append(i + j + k + z)
        return res


x = Solution()
dig = input()
print(x.letterCombinations(dig))
