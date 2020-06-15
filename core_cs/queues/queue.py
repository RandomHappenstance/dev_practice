class Queue:

    def __init__(self):
        self.queue = []

    def is_empty(self):
        """ Returns a boolean for the size of the queue.
        Args:
            None

        Returns:
            A boolean corresponding to the size of the queue. It
            will return False if the queue has one or more
            elements, and True if the queue is empty.
        """

        if len(self.queue) == 0:
            return True
        else:
            return False

    def push(self, value):
        self.queue.insert(0, value)

    def pop(self):
        return self.queue.pop()

    def peek(self):
        if len(self.queue) == 0:
            return None
        else:
            return self.queue[0]
    
