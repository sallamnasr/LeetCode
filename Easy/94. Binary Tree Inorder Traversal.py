
from typing import Optional
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # def x(self,node) :
    #     res = []
    #     if node :
    #         self.x(node.left)
    #         res.append(node.val)
    #         self.x(node.right)
    #     return res
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root :
            res += self.inorderTraversal(root.left)
            res.append(root.val)
            res += self.inorderTraversal(root.right)
        return res 
        
x = Solution()
print(x.inorderTraversal([1,None,2,3]))