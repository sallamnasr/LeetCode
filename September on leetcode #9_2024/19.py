from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        res = []
        for x in range(len(expression)):
            if expression[x] in '+-*':
                left = self.diffWaysToCompute(expression[:x])
                right = self.diffWaysToCompute(expression[x+1:])

                for l in left:
                    for r in right:
                        if expression[x] == '+':
                            res.append(l + r)
                        elif expression[x] == '-':
                            res.append(l - r)
                        elif expression[x] == '*':
                            res.append(l * r)

        if not res:
            res.append(int(expression))

        return res
