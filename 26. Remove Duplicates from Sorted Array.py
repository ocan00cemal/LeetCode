class Solution:
    def removeDuplicates(self, nums) -> int:
        n = len(nums)
        if n < 2:
            return n
        i = 0
        j = 1
        counter = 0
        
        while j < n:
            
            if nums[i] == nums[j]:
                del nums[j]
                nums.append("-")
                counter += 1
            else:
                i += 1
                j += 1
            if nums[i] == "-":
                break
                
        return n - counter