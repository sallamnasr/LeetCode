# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = n
        while l < r:
            mid = l + (r-l)//2
            res = isBadVersion(mid)
            if res:
                r = mid
            else:
                l = mid + 1
        return l