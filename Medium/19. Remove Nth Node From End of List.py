# Definition for singly-linked list.
from types import Optional 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ln = 0 
        curr = head
        while curr :
            ln += 1 
            curr = curr.next 
        n = ln - n + 1 
        curr = head 
        prev = None 
        while n-1 > 0 :
            prev = curr 
            curr = curr.next 
            n -= 1
        if prev :
            prev.next = curr.next 
        else :
            head = curr.next
        return head 