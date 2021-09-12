class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        else:
            for i in range(len(s)//2):
                for rep in (("()",""),("[]",""),("{}","")):
                    s = s.replace(*rep)
            if len(s):
                return False
            else:
                return True
