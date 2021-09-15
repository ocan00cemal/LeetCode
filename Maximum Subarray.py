class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        max_total = 0

        for num in nums:
            if total + num <= 0:
                if total >= max_total:
                    max_total = total
                total = 0

            elif total + num > 0:
                total += num
                if total >= max_total:
                    max_total = total

        if max_total == 0:
            return max(nums)
        else:
            return max_total