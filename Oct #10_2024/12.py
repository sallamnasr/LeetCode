from typing import List
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        lst = []
        for x in intervals :
            lst.append((x[0],1))
            lst.append((x[1]+1,-1))
        lst.sort()
        cnt = 0 
        mx = cnt 
        for x in lst :
            if x[1] == 1 :
                cnt += 1 
            else :
                cnt -= 1 
            mx = max(mx,cnt)
        return mx 
    
    
x = Solution()
print(x.minGroups(intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]))