class Solution:
    def isValid(self, s: str) -> bool:
        stack = {
            '(' : ')',
            '[' : ']',
            '{' : '}'
        }
        arr = []
        for ch in s :
            if ch in stack :
                arr.append(ch)
            elif arr and ch in stack.values() :
                if stack[arr[-1]] == ch :
                    arr.pop()
                else :
                    return False
        return len(arr)==0
                
            
            
            
x = Solution()
s = input()
print(x.isValid(s))