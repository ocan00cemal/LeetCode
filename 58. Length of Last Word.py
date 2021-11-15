class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        counter = 0
        i = -1
        n = len(s)

        while abs(i) <= n:
            if s[i] == " " and counter == 0:
                i -= 1
            elif s[i] != " ":
                counter += 1
                i -= 1
            elif s[i] == " " and counter != 0:
                break

        return counter
