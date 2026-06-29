class MinStack:

    def __init__(self):
        # Store the (val, min) in stack
        self.stack = []
        

    def push(self, val: int) -> None:
        
        block = tuple()
        if not self.stack:
            block = (val, val)
        else:
            prev_min = self.stack[-1][1]
            block = (val, min(val, prev_min))

        self.stack.append(block)

        return None
        

    def pop(self) -> None:
        if not self.stack:
            return None

        self.stack = self.stack[:-1]
        

    def top(self) -> int:
        # Better to have a check on stack
        if not self.stack:
            return None
        
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        # Better to have a check on mins
        if not self.stack:
            return None
        
        return self.stack[-1][1]
        
