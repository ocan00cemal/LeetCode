class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        n = len(nums)
        
        while i < n:
            if nums[i] == 0:
                j = i
                while j < n:       
                    if nums[j] != 0:
                        nums[i], nums[j] = nums[j], nums[i]
                        break
                    else:
                        j += 1
            i += 1