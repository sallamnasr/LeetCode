from typing import List


class Solution:
    def binary_search(self, arr: List[int], x: int) -> bool:
        l = 0
        r = len(arr) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if arr[mid] == x:
                return True
            elif arr[mid] < x:
                l = mid + 1
            else:
                r = mid - 1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if self.binary_search(row, target):
                return True
        return False
