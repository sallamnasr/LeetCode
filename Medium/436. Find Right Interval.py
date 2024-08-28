from typing import List
# class Solution:
#     def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
#         ans = []
#         n = len(intervals)
#         for end in range(n):
#             min_start = float('inf')
#             index = -1 
#             for start in range(n):
#                 if intervals[end][1] <= intervals[start][0]:
#                     if intervals[start][0] < min_start:  
#                         min_start = intervals[start][0]
#                         index = start
#             ans.append(index if index != -1 else -1)

#         return ans
    

class Solution:
    def binary_search(self, starts, target):
        if target > starts[-1][0]:
            return -1 
        
        l, r = 0, len(starts) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if starts[mid][0] == target:
                return starts[mid][1]
            elif starts[mid][0] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return starts[l][1] if l < len(starts) else -1
            
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        ans = []
        n = len(intervals)
        starts = sorted((interval[0], i) for i, interval in enumerate(intervals))
        
        for i in range(n):
            target = intervals[i][1] 
            ans.append(self.binary_search(starts, target))
        return ans

        
x = Solution()
print(x.findRightInterval([[1,4],[2,3],[3,4]]))