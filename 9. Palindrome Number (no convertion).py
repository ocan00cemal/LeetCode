from math import log10, ceil


class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x == 0:
            return True
        elif x < 0 or x % 10 == 0:
            return False

        num_list = []
        n = ceil(log10(x))

        for i in range(n):
            num_list.append(x // pow(10, i) % 10)

        if num_list == list(reversed(num_list)):
            return True
        else:
            return False
