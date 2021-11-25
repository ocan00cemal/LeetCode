class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dic = {}
        result = 0
        for j in jewels:
            dic[j] = 0

        for s in stones:
            if s in dic.keys():
                result += 1

        return result
