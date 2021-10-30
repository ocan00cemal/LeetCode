class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        if ruleKey == "type":
            i = 0
        elif ruleKey == "color":
            i = 1
        else:
            i = 2

        count = 0

        for sub_list in items:
            if sub_list[i] == ruleValue:
                count += 1
        return count
