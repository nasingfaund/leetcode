class MinStack:

    def __init__(self):
        self.stack = [] # has val, and current_min
        
    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            last_val, last_min = self.stack[-1]
            if val < last_min:
                self.stack.append((val, val))
            else:
                self.stack.append((val, last_min))
        
    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
    
class MinStack:
    def __init__(self):
        self.alist = []
        self.min = []

    def push(self, x: int) -> None:
        if not self.min:
            self.min.append(x)
        if self.alist:
            if x <= self.min[-1]:
                self.min.append(x)
        self.alist.append(x)
        

    def pop(self) -> None:
        elem = self.alist.pop()
        if elem == self.min[-1]:
            self.min.pop()
        return elem
        

    def top(self) -> int:
        return self.alist[-1]
        

    def getMin(self) -> int:
        return self.min[-1]
        
