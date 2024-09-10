from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        matrix = [[None for _ in range(n)] for _ in range(n)]
        dir = 0
        i, j = 0, 0
        siz = 1
        while siz <= n**2 :
            matrix[i][j] = siz
            newi = i + directions[dir][0]
            newj = j + directions[dir][1]
            if newi < 0 or newi >= len(matrix) or newj < 0 or newj >= len(matrix[0]) or matrix[newi][newj] is not None:
                dir = (dir+1) % 4
                newi = i + directions[dir][0]
                newj = j + directions[dir][1]
            i = newi
            j = newj
            siz += 1

        return matrix


x = Solution()
print(x.generateMatrix(3))