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


def x(n, a: str, b: str):
    if n == 2:
        a = a[::-1]
        b = b[::-1]
        if a > b:
            print('YES')
            print(1, 2)
        else:
            print("NO")
        return
    if a[0] > b[0]:
        print("YES")
        print(2, 3)
        return
    for i in range(1, n):
        if a[i] > b[i]:
            print("YES")
            print(1, i+1)
            return
    print("NO")
    return


if __name__ == '__main__':
    t = 1 
    # t = int(input())
    for _ in range(t):
        n = int(input())
        a = input()
        b = input()
        x(n, a, b)
