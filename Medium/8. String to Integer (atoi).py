class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:  
            return 0
        res = 0
        s_res = ""
        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        start_idx = 0
        
        if s[0] == '-' or s[0] == '+':
            start_idx = 1

        for i in range(start_idx, len(s)):
            if s[i] in digits:
                s_res += s[i]
            else:
                break

        if not s_res:  
            return 0

        res = int(s_res)

        if s[0] == '-':
            res = -res

        # Clamp result within the 32-bit signed integer range
        if res >= (2**31):
            return (2**31) - 1
        elif res < -2**31:
            return -2**31

        return res
