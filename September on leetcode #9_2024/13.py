from typing import List
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        for i in range(1,len(arr)):
            arr[i] = arr[i-1]^arr[i]
        result = []
        for q in queries :
            if q[0] == 0 :
                result.append(arr[q[1]])
            else :
                result.append(arr[q[1]] ^ arr[q[0]-1])
            
        return result
x = Solution()
print(x.xorQueries([1, 3, 4, 8], [[0, 1], [1, 2], [0, 3], [3, 3]]))

# [1,3,4,8] -> arr 
# [1,2,6,14] -> Prefix Xor 
# 3^4 = 6^1
# 4^8 = 14^2