import math
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        x = math.sqrt(num)
        return int(x)**2 == num
    
    
x = Solution()
print(x.isPerfectSquare(16))