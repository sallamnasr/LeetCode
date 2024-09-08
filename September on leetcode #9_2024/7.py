from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def DFS(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool :
        if not head :
            return True
        if not root :
            return False 
        if root.val != head.val :
            return False 
        return self.DFS(head.next , root.left) or self.DFS(head.next , root.right)
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not root :
            return False
        if self.DFS(head,root) :
            return True
        return self.isSubPath(head,root.left) or self.isSubPath(head,root.right) 
        
