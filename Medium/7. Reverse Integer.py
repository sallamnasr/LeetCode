
class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = (2**31) - 1
        INT_MIN = -1 * (2**31)

        if x < 0:
            x = str(x)
            x = x[:0:-1]
            reversed_x = -1 * int(x)
        else:
            x = str(x)
            x = x[::-1]
            reversed_x = int(x)

        if reversed_x < INT_MIN or reversed_x > INT_MAX:
            return 0
        else:
            return reversed_x

a = Solution()
print(a.reverse(264)) #462
print(a.reverse(-264)) #-426
print(a.reverse(260)) #62
