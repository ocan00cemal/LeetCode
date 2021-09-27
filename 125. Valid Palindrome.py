class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s_new = ""

        for i in s:
            if i in "abcdefghijklmnopqrstuvwxyz0123456789":
                s_new += i

        s_new_list = list(s_new)
        return s_new_list == list(reversed(s_new_list))
