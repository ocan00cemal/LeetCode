class Solution:
    def maxArea(self, height) -> int:
        n = len(height)
        left = 0
        right = n - 1
        max_volume = 0

        while left != right:
            temp = (right - left) * min(height[left], height[right])
            if temp > max_volume:
                max_volume = temp
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_volume
