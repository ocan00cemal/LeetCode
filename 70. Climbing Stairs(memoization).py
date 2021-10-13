class Solution:
    def climbStairs(self, n: int) -> int:
        #  Actually, this question looks like a fibonacci sequence problem

        dict_fibo = {}

        def fibo(m):
            if m in dict_fibo:
                return dict_fibo[m]
            elif m == 1:
                return 1
            elif m == 2:
                return 2
            
            total = fibo(m - 1) + fibo(m - 2)
            dict_fibo[m] = total
            return total

        return fibo(n)
