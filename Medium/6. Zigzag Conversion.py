class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        result = [''] * numRows 
        down = False
        up = False 
        idx = 0 
        
        for ch in s :
            result[idx] += ch 
            if idx == 0 :
                down = True 
                up = False
            if idx == numRows - 1 :
                up = True 
                down = False
            
            if up :
                idx -= 1 
            if down :
                idx += 1 
            
        return ''.join(result)
        
        
x = Solution()
s = "PAYPALISHIRING"


print(x.convert(s, 4))
