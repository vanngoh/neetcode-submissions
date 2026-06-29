class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.mins:
            self.mins.append(val)
            return None
        
        # If this is not the first value
        # Do the values comparison with previous min
        prev_min = self.mins[-1]
        if val <= prev_min:
            self.mins.append(val)
        else:
            self.mins.append(prev_min)

        return None
        

    def pop(self) -> None:
        if not self.stack:
            return None

        self.stack = self.stack[:-1]
        self.mins = self.mins[:-1]
        

    def top(self) -> int:
        # Better to have a check on stack
        if not self.stack:
            return None
        
        return self.stack[-1]
        

    def getMin(self) -> int:
        # Better to have a check on mins
        if not self.mins:
            return None
        
        return self.mins[-1]
        
