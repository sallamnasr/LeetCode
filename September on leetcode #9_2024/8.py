from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        cnt = 0
        temp = head
        while temp:
            temp = temp.next
            cnt += 1

        temp = head
        res = []

        if k >= cnt:
            while temp:
                res.append(ListNode(temp.val))
                temp = temp.next
            for _ in range(k - cnt):
                res.append(None)  
        else:
            division = cnt // k  
            remind = cnt % k 

            for i in range(k):
                curr = temp
                part_size = division + (1 if remind > 0 else 0)
                remind -= 1

              
                for j in range(part_size - 1):
                    if temp:
                        temp = temp.next

                if temp:
                    next_part = temp.next
                    temp.next = None  
                    temp = next_part  

                res.append(curr)
                
        return res

if __name__ == "__main__" :
    x = Solution()
    print(x.splitListToParts([1,2,3],5))