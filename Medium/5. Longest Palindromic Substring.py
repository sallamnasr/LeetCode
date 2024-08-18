class Solution:

    def longestPalindrome(self, s: str) -> str:
        def is_palindrome(sub: str) -> bool:
            return sub == sub[::-1]

        n = len(s)
        longest_palindrome = ""
        
        for i in range(n):
            for j in range(i, n):
                substring = s[i:j+1]
                if is_palindrome(substring) and len(substring) > len(longest_palindrome):
                    longest_palindrome = substring

        return longest_palindrome


# child = Solution()
# s = input("Enter a string: ")
# print(child.longestPalindrome(s))
