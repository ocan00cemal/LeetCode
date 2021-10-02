class Solution:
    def twoSum(self, nums, target):

        sorted_nums = sorted(nums)
        i = 0
        j = -1

        while i != j:
            total = sorted_nums[i] + sorted_nums[j]

            if total == target:
                idx_first = nums.index(sorted_nums[i])
                nums[idx_first] = "temp"
                idx_second = nums.index(sorted_nums[j])
                return [idx_first, idx_second]

            else:
                if total > target:
                    j -= 1
                else:
                    i += 1
