class Solution:
    from typing import List

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        temp = nums1[:m]
        i, j = 0, 0

        for k in range(len(nums1)):
            if i < m and (j >= n or temp[i] <= nums2[j]):
                nums1[k] = temp[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
        return nums1


x = Solution()
print(x.merge([0], 0, [1], 1))
