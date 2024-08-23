# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def inorder_traversal(root ,arr) :
            if root :
                inorder_traversal(root.left ,arr)
                arr.append(root.val)
                inorder_traversal(root.right , arr)
        
        x = []
        y = []
        inorder_traversal(p,x)
        inorder_traversal(q,y)
        return x==y
            
