class Solution:
    def maximumSwap(self, num: int) -> int:
        def GetLarge(lst):
            mx = lst[0]
            index = 0
            for i in range(len(lst)):
                if lst[i] >= mx:
                    mx = lst[i]
                    index = i
            return mx, index

        num = list(str(num))
        largest = sorted(num, reverse=True)

        for i in range(len(num)):
            large, large_idx = GetLarge(num[i:])
            large_idx += i

            if largest[i] != num[i]:
                num[i], num[large_idx] = num[large_idx], num[i]
                break

        return int("".join(num))


x = Solution()
print(x.maximumSwap(52525))
