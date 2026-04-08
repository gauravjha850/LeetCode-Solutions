from collections import deque

class MyStack(object):

    def __init__(self):
        # Initialize a deque to act as our queue
        self.q = deque()

    def push(self, x):
        self.q.append(x)
        # To maintain stack order, rotate the queue
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self):
        return self.q.popleft()

    def top(self):
        return self.q[0]

    def empty(self):
        return not self.q