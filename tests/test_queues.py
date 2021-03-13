import unittest

from core_cs.queues.queue import Queue


class QueueTesting(unittest.TestCase):

    def test_instantiation(self):
        """ Testing the instantiation of a Queue """
        # Test that the object is of type Queue.
        queue = Queue()
        assert isinstance(queue, Queue)

    def test_push(self):
        """ Testing an initialized queue's push function """
        # Pushing a value into an empty queue.
        queue = Queue()
        queue.push('first')
        assert queue.peek() == 'first'

        # Pushing a second value into the queue.
        queue = Queue()
        queue.push('first')
        queue.push('second')
        assert queue.peek() == 'second'

    def test_peek(self):
        """ Testing the peek function in a queue """
        # Peek at the indexed value in an empty queue.
        queue = Queue()
        assert queue.peek() == None

        # Peek at the indexed value on a non-empty queue.
        queue = Queue()
        queue.push('first')
        assert queue.peek() == 'first'

        queue = Queue()
        queue.push('first')
        queue.push('second')

        queue.pop()
        assert queue.peek() == 'second'

    def test_pop(self):
        """Testing the pop function in a queue """
        queue = Queue()
        queue.push('first')
        queue.push('second')

        queue.pop()
        assert queue.peek() == 'second'

    def test_is_empty(self):
        """ Testing the boolean funtion is_empty """
        # Test that after initialization the queue is empty.

        queue = Queue()
        assert queue.is_empty() == True

        # Test after pushing an element that the queue is NOT empty
        queue = Queue()
        queue.push('first')
        assert queue.is_empty() == False