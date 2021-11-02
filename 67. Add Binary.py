class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = -1
        total = ""
        carry = 0
        diff = len(a) - len(b)

        if diff > 0:
            b = diff * "0" + b
        elif diff < 0:
            a = abs(diff) * "0" + a

        while abs(i) <= len(a):
            if int(a[i]) + int(b[i]) + carry < 2:
                total = str(int(a[i]) + int(b[i]) + carry) + total
                carry = 0
            elif int(a[i]) + int(b[i]) + carry == 2:
                carry = 1
                total = "0" + total
            else:
                carry = 1
                total = "1" + total
            i -= 1

        if carry:
            total.replace(total[0], "0")
            total = "1" + total

        return total
