from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        p1, p2 = 0, 0
        n = len(nums1) + len(nums2)
        res = []
        x = n // 2 + 1

        for i in range(x):
            if p1 < len(nums1) and (p2 >= len(nums2) or nums1[p1] < nums2[p2]):
                res.append(nums1[p1])
                p1 += 1
            else:
                res.append(nums2[p2])
                p2 += 1

        if n % 2:
            return res[-1]
        else:
            return (res[-1] + res[-2]) / 2



# x = Solution()
# print(x.findMedianSortedArrays([1, 3], [2])) 
