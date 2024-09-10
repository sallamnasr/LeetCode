from typing import List 
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        dir = 0 
        i,j = 0,0
        result = []
        siz = len(matrix)*len(matrix[0])
        while siz :
            result.append(matrix[i][j])
            matrix[i][j] = None 
            newi = i + directions[dir][0]
            newj = j + directions[dir][1]
            if newi<0 or newi>=len(matrix) or newj<0 or newj>=len(matrix[0])or matrix[newi][newj] is None :
                dir = (dir+1)%4
                newi = i + directions[dir][0]
                newj = j + directions[dir][1]
            i = newi 
            j = newj
            siz -= 1
            
        return result


x = Solution()
print(x.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))