class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False

        x_list = [int(x) for x in str(x)]
        x_list_reversed = reversed(x_list)

        if list(x_list_reversed) == x_list:
            return True
        else:
            return False
