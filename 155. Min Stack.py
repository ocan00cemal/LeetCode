class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if self.stack == []:
            self.stack.append([val, val])
        else:
            if self.stack[-1][1] >= val:
                self.stack.append([val, val])
            else:
                self.stack.append([val, self.stack[-1][1]])

    def pop(self) -> None:
        if len(self.stack) > 0:
            del self.stack[-1]

    def top(self) -> int:
        if len(self.stack) == 0:
            return None
        return self.stack[-1][0]

    def getMin(self) -> int:
        if len(self.stack) == 0:
            return None
        return self.stack[-1][1]
