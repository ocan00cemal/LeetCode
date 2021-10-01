class Solution:
    def maxProfit(self, prices) -> int:
        cur_min = prices[0]
        max_profit = 0

        for i in prices:
            if i < cur_min:
                cur_min = i
            else:
                max_profit = max(max_profit, i - cur_min)

        return max_profit
