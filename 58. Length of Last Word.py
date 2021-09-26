class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        counter = 0
        i = -1
        while True:
            try:
                if s[i] == " " and counter == 0:
                    i -= 1
                elif s[i] != " ":
                    counter += 1
                    i -= 1
                elif s[i] == " " and counter != 0:
                    return counter
            except:
                return counter
