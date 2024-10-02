from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if not arr:  # Handle the empty list case
            return []

        nums = arr[:]
        nums.sort()

        mp = {}
        cnt = 1
        prev = nums[0]
        mp[prev] = 1
        for i in range(1, len(nums)):
            if prev != nums[i]:
                cnt += 1
                prev = nums[i]
            mp[nums[i]] = cnt

        res = []
        for i in range(len(arr)):
            res.append(mp[arr[i]])
        return res


x = Solution()
print(x.arrayRankTransform([40, 10, 20, 30]))  # Output: [4, 1, 2, 3]
print(x.arrayRankTransform([]))  # Output: []
