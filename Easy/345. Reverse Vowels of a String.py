# class Solution:
#     def reverseVowels(self, s: str) -> str:
#         s = list(s)
#         vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
#         string = ''
#         for i in range(len(s)):
#             if s[i] in vowels:
#                 string += s[i]
#                 s[i] = '_'
#         string = string[::-1]
#         j = 0
#         for i in range(len(s)):
#             if s[i] == '_' and j < len(string):
#                 s[i] = string[j]
#                 j += 1
#         return ''.join(s)

