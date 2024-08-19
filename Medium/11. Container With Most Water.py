from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        mx = 0
        while l <= r:
            area = (r - l) * min(height[l], height[r])
            mx = max(mx, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return mx



# x = Solution()
# arr = list(map(int,input().split()))
# print(x.maxArea(arr))