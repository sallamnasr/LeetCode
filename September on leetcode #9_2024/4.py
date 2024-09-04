# 874. Walking Robot Simulation ->>> Medium
from typing import List
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        st = set(map(tuple, obstacles))
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        mx = 0
        dir = 0
        x, y = 0, 0
        for command in commands:
            if command == -1:
                dir += 1
            elif command == -2:
                dir -= 1
            else:
                dir = ((dir % 4)+4) % 4
                newx, newy = directions[dir]
                for _ in range(command):
                    if (x+newx, y+newy) not in st:
                        x += newx
                        y += newy
                    else:
                        break
                mx = max(mx, x**2 + y**2)
        return mx


x = Solution()
print(x.robotSim([6, -1, -1, 6], []))


# North means + Y direction.  0
# East means + X direction.   1
# South means - Y direction.  2
# West means - X direction.   3
