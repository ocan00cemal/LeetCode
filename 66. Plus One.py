class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1    
        i = -1
        
        while digits[i] >= 10:
            digits[i] = 0
            if len(digits) == abs(i):
                digits.insert(0,1)
            else:    
                i -=1
                digits[i] += 1

        return digits
        