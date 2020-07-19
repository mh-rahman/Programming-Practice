class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.pushS = []
        self.popS = []
        
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.pushS.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.popS:
            while self.pushS:
                self.popS.append(self.pushS.pop())
        return self.popS.pop()
        
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.popS[-1] if self.popS else self.pushS[0]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.popS) == 0 and len(self.pushS) == 0
        
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()