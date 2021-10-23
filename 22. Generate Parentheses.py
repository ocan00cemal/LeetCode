class Solution:
    def generateParenthesis(self, n: int):
        res = []

        def rec(cur="", openC=0, closedC=0):

            if openC == closedC == n:
                res.append(cur)
                return

            if openC < n:

                rec(cur + "(", openC + 1, closedC)

            if openC > closedC:

                rec(cur + ")", openC, closedC + 1)

        rec()
        return res
