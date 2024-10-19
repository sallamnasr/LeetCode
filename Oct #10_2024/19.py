class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def inverter(s):
            res = ''
            for bit in s:
                if bit == '1':
                    res += '0'
                else:
                    res += '1'
            return res

        nn = ['0', '011', '0111001', '011100110110001']
        for i in range(5, 21):
            invert = inverter(nn[-1])
            reverse = ''.join(reversed(invert))
            s = nn[-1] + '1' + reverse
            nn.append(s)

        return nn[n-1][k-1]


x = Solution()
print(x.findKthBit(3, 1))
