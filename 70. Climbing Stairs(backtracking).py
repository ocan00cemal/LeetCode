class Solution:
    def climbStairs(self, n: int) -> int:
        total = [0]

        def rec(cur=0):
            if cur == n:
                total[0] += 1
                return
            if cur + 1 <= n:
                rec(cur + 1)
            if cur + 2 <= n:
                rec(cur + 2)

        rec()
        return total[0]
