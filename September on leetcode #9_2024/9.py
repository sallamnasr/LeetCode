from typing import List,Optional
from collections import deque
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        dir = 0
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        grid = [[-1 for _ in range(n)] for _ in range(m)]
        i,j = 0,0
        while head :
            grid[i][j] = head.val
            newi = i + directions[dir][0]
            newj = j + directions[dir][1]
            if newj>=n or newj<0 or newi>=m or newj<0 or grid[newi][newj] != -1 :
                dir = (dir+1)%4
                newi = i + directions[dir][0]
                newj = j + directions[dir][1]
            i = newi 
            j = newj
            head = head.next
        return grid
    
x = Solution()
print(x.spiralMatrix(3,5,[3,0,2,6,8,1,7,9,4,2,5,5,0]))
        
            

        