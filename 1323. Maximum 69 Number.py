class Solution:
    def maximum69Number(self, num: int) -> int:
        str_list = []
        for i in str(num):
            str_list.append(i)

        for i, char in enumerate(str_list):
            if char != "9":
                str_list[i] = "9"
                break

        return int("".join(str_list))
