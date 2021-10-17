class Solution:
    def majorityElement(self, nums):
        nums.sort()
        maj_ele = [nums[0], 0]
        n = len(nums)

        for i in nums:
            if i == maj_ele[0]:
                maj_ele[1] += 1
            else:
                if maj_ele[1] >= n / 2:
                    return maj_ele[0]
                else:
                    maj_ele = [i, 1]

        return maj_ele[0]
