class Solution:
    def threeSumClosest(self, nums, target) -> int:
        n = len(nums)
        nums.sort()
        i = 0  # left pointer
        k = i + 1
        j = n - 1  # right pointer

        closest = nums[i] + nums[j] + nums[k]

        for i in range(n - 2):
            k = i + 1
            j = n - 1
            while k != j:
                temp = nums[i] + nums[j] + nums[k]

                if abs(target - closest) > abs(target - temp):
                    closest = temp

                if temp > target:
                    j -= 1
                elif temp < target:
                    k += 1
                else:
                    return closest

        return closest
