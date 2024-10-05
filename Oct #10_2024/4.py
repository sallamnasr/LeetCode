from typing import List


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        sm = skill[0] + skill[-1]
        total_ch = 0
        l, r = 0, len(skill)-1
        while l <= r:
            new_sm = skill[l] + skill[r]
            if new_sm != sm:
                return -1
            sm = new_sm
            total_ch += (skill[l]*skill[r])
            l += 1
            r -= 1
        return total_ch


x = Solution()
print(x.dividePlayers([3, 2, 5, 1, 3, 4]))
