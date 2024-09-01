# 2022. Convert 1D Array Into 2D Array -> easy 
from typing import List
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        siz = len(original)
        if siz != n*m :
            return []
        arr_2d = [[0]*m for _ in range(n)]
        i = 0
        for row in range(n) :
            for col in range(m) :
                arr_2d[row][col] = original[i]
                i += 1 
        return arr_2d