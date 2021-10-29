class Solution:
    def nextPermutation(self, nums) -> None:
        if len(nums) <= 1:
            return

        def change(left, right):
            nums[left], nums[right] = nums[right], nums[left]
            ext = sorted(nums[left + 1 :])
            del nums[left + 1 :]
            nums.extend(ext)

        i = -2
        while abs(i) <= len(nums):
            j = -1
            while j > i:
                if nums[j] > nums[i]:
                    change(i, j)
                    return
                j -= 1
            i = i - 1

        if min(nums) == nums[0]:
            min_after = min(nums[1:])
            min_idx = nums.index(min_after)
            change(0, min_idx)

        elif max(nums) == nums[0]:
            nums.reverse()
