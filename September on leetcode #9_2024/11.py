class Solution:
    def BinaryBits(self, num: int) -> str:
        res = ''
        while num:
            bit = num % 2
            num //= 2
            res += str(bit)
        return ''.join(reversed(res))

    def minBitFlips(self, start: int, goal: int) -> int:
        start = self.BinaryBits(start)
        goal = self.BinaryBits(goal)
        cnt = 0
        mn = min(len(start),len(goal))
        mx = max(len(start),len(goal))
        dif = mx-mn
        x = '0'*dif 
        if mn == len(start) : 
            start = x + start
        else :
            goal = x + goal
        for i in range(mx) :
            if goal[i] != start[i] :
                cnt += 1
        return cnt 
            

x = Solution()
print(x.minBitFlips(10,7))
