class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        while self.s1:
            self.s2.append(self.s1.pop())
        
        self.s2.append(x)
        
        while self.s2:
            self.s1.append(self.s2.pop())
        return self.s1
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.s1:
            raise
        return self.s1.pop()
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        while self.s1:
            self.s2.append(self.s1.pop())
        p = self.s2[0]
        while self.s2:
            self.s1.append(self.s2.pop())
        return p
        
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not bool(self.s1)
        
