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
        
