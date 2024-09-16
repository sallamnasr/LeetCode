from typing import List
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints = ["23:59", "00:01", "22:58", "00:00"]
        hours = []
        for x in timePoints:
            time = (int(x[:2]), int(x[3:]))
            hours.append(time)

        hours.sort()

        diff = []

        first_time = hours[0]
        last_time = hours[-1]

        first_in_minutes = first_time[0] * 60 + first_time[1]
        last_in_minutes = last_time[0] * 60 + last_time[1]

        diff.append(min((first_in_minutes + 1440 - last_in_minutes),
                    (last_in_minutes - first_in_minutes)))

        for i in range(1, len(hours)):
            current_time = hours[i][0] * 60 + hours[i][1]
            previous_time = hours[i-1][0] * 60 + hours[i-1][1]
            minutes_diff = current_time - previous_time
            diff.append(minutes_diff)
        return min(diff)
