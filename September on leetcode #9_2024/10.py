import math
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        dummy.next = head 
        prev,curr = head,head.next
        
        while curr :
            neww = ListNode(math.gcd(prev.val , curr.val))
            neww.next = prev.next 
            prev.next = neww
            # _____
            prev = curr 
            curr = curr.next 
        return dummy.next
            
x = Solution()
print(x.insertGreatestCommonDivisors([18,6,10,3]))

        