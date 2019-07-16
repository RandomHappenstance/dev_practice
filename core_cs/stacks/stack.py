class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        # Had to look up if a Python list had a pop function.[1]
        self.stack.pop()

    def peek(self):
        # Had some problems remembering how to select the last element in a
        # list. The [:] notation is called the 'Slicing Operator'. 
        # 
        # The best explanation I found on this topic is through Stack Overflow[2]
        # where the person who replied with:
        #
        # a[start:stop:step]
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[-1]
        
    
# References
# 1.https://docs.python.org/2/tutorial/datastructures.html
# 2.https://stackoverflow.com/questions/509211/undersatnding-slice-notation
