from typing import List


class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        target = times[targetFriend]
        times.sort(key=lambda x: x[0])
        chairs = [0] * len(times)

        for time in times:
            arrive, leave = time
            for i in range(len(chairs)):
                if chairs[i] <= arrive:
                    if time == target:
                        return i
                    chairs[i] = leave
                    break



x = Solution()
print(x.smallestChair(times=[[3, 10], [1, 5], [2, 6]], targetFriend=0))
