class Solution:
    def searchInsert(self, nums, target):

        i = 0
        j = len(nums) - 1

        while True:

            if target == nums[i] or target < nums[i]:
                return i
            elif target == nums[j]:
                return j
            elif target > nums[j]:
                return j + 1

            n = (i + j) // 2

            if target < nums[n]:
                j = n
            elif target > nums[n]:
                i = n + 1
            else:
                return n
