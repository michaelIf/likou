# 155
# 使用list
class MinStack:

    def __init__(self):
        self.stack = list()
        """
        initialize your data structure here.
        """
    def push(self, x: int) -> None:
        self.stack.append(x)
    def pop(self) -> None:
        if len(self.stack) == 0:
            return None
        else:
            self.stack.pop()
    def top(self) -> int:
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[-1]
    def getMin(self) -> int:
        if len(self.stack) == 0:
            return None
        else:
            return min(self.stack)

# 使用辅助栈
class MinStack2:
    def __init__(self):
        import math
        self.stack = []
        self.min_stack = [math.inf]
    def push(self, x):
        self.stack.append(x)
        self.min_stack.append(min(x, self.min_stack[-1]))
    def pop(self):
        self.stack.pop()
        self.min_stack.pop()
    def top(self):
        return self.stack[-1]
    def getMin(self):
        return self.min_stack[-1]