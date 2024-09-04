class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 1, n
        while l <= r:
            mid = l + (r - l) // 2
            pref_mid = mid * (mid + 1) // 2
            if pref_mid == n:
                return mid
            elif pref_mid < n:
                l = mid + 1
            else:
                r = mid - 1
        return r 

# x = Solution()
# print(x.arrangeCoins(2))