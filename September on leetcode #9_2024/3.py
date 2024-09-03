# 1945. Sum of Digits of String After Convert---->>>Easy
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        nums = ''
        for i in range(len(s)):
            num = str(ord(s[i]) - 96)
            nums += num
        for _ in range(k):
            summ = 0
            for x in nums:
                summ += int(x)
            nums = str(summ)
        return int(nums)


x = Solution()
print(x.getLucky('zbax', 2))
