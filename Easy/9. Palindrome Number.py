# This soluion without convertion the number to string 


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            arr = []
            while x != 0:
                arr.append(x % 10)
                x //= 10
            return arr[::1] ==arr[::-1]
        
        
# This soluion that convert the number to string


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            x = str(x)
            return x[::1] == x[::-1]