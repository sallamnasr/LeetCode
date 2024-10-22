from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        q = deque([root])
        
        while q :
            sm = 0 
            n = len(q)
            
            for _ in range(n) :
                node = q.popleft()
                sm += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            arr.append(sm)
        if k > len(arr) :
            return -1 
        arr.sort(reverse=True)
        return arr[k-1]
