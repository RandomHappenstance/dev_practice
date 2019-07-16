# Title: Stacks and Queues
#
# Stacks
# A stack is a data structure that that follows Last In First Out (LIFO) 
# access. The easiest way to think about it is to think about it as, well,
# stacking dishes. The rule in accessing it is that you cannot pull from
# any other position than the top.
#
# 
#                                   ------- <-  
#                    ------- <-     -------       ------- <-
#  1. ------- <-  2. -------     3. -------    4. ------- 
#
# In the picture above, the '<-' is the element in memory that can be 
# accessed.
#
# Stacks have the following functions:
#  * Push
#  * Pop
#  * Is stack empty
#  * Peek
# 
#
# Implementation

import unittest

class StackTesting(unittest.TestCase):
    
    def test_instantiation(self):
        """ Testing the instantiation of a Stack """
        # Test that the object is of type Stack.
        stack = Stack()
        assert isinstance(stack, Stack)

    def test_push(self, value):
        """ Testing an initialized stack's push function."""
        # Pushing a value into an empty stack.
        stack = Stack()
        stack.push('first')
        assert stack.peek() === 'first'

        # Pushing a second value into the stack.
        stack = Stack()
        stack.push('first')
        stack.push('second')
        assert stack.peek() == 'second'


    def test_peek(self):
        """ Testing the peek function in a stack  """
        # Peek at the indexed value in an empty stack.
        stack = Stack()
        assert stack.peek() == None 

        # Peek at the indexed value on a non-empty stack.
        stack = Stack()
        stack.push('first')
        assert stack.peek() == 'first'

        stack = Stack()
        stack.push('first')
        stack.push('second')
       
        stack.pop()
        assert stack.peek() == 'first'

    def test_pop(self):
        """Testing the pop function in a stack."""
        stack = Stack()
        stack.push('first')
        stack.push('second')
       
        stack.pop()
        assert stack.peek() == 'first'

    def test_is_empty(self):
        """ Testing the boolean funtion is_empty """
        # Test that after initialization the stack is empty.
        
        stack = Stack()
        assert stack.is_empty() == True

        # Test after pushing an element that the stack is NOT empty
        stack = Stack()
        stack.push('first')
        assert stack.is_empty() == 'False'

