class Solution:
    def myAtoi(self, s: str) -> int:
        neg = False
        num_to_return = "0"
        for c in s:
            if c == " ":
                s = s[1:]
            else:
                break

        if s == "":
            return 0
        elif s[0] == "-":
            neg = True
            s = s[1:]
        elif s[0] == "+":
            s = s[1:]

        for c in s:
            if c in "0123456789":
                num_to_return += c
            else:               
                break

        num_to_return = int(num_to_return)
        if neg:
            num_to_return =  -num_to_return

        if num_to_return >= pow(2, 31):
            return pow(2, 31) - 1
        elif num_to_return <= pow(-2, 31):
            return pow(-2, 31)
        else:
            return num_to_return
