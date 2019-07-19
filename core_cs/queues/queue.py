class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False

    def push(self, value):
        self.queue.append(value)

    def pop(self):
        self.queue.pop()

    def peek(self):
        if len(self.queue) == 0:
            return None
        else:
            return self.queue[0]
        
    
# References
# 1. 
