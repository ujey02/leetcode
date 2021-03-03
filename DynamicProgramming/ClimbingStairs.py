# 95.2 / 47.43
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        else:
            p1, p2 = 1, 2
            for _ in range(n-2):
                p1, p2 = p2, p1 + p2
            return p2
