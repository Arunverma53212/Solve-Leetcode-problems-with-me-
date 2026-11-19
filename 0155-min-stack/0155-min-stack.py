class MinStack:

    def __init__(self):
        self.MinStack = []

    def push(self, value: int) -> None:
        if len(self.MinStack)==0:
            self.MinStack.append([value,value])
        else:
            mini = min(value,self.MinStack[-1][1])
            self.MinStack.append([value,mini])

    def pop(self) -> None:
        self.MinStack.pop()

    def top(self) -> int:
        return self.MinStack[-1][0]
        
        
    def getMin(self) -> int:
        return self.MinStack[-1][1]

        


        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna