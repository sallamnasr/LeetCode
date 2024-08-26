from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        st = set(letters)
        letters = sorted(st)
        l = 0
        r = len(letters) - 1
        if letters[l] > target or letters[r] <= target:
            return letters[l]

        while l <= r:
            mid = l + (r-l)//2
            if letters[mid] == target:
                return letters[mid + 1]
            elif letters[mid] < target:
                l = mid
            else:
                r = mid

            if r-l == 1:
                return letters[r]


# link :
#     https://leetcode.com/problems/find-smallest-letter-greater-than-target/?envType =study-plan-v2&envId=binary-search