#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-05-05 13:29:44
# Title      :  155 min stack

# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

#    push(x) -- Push element x onto stack.
#    pop() -- Removes the element on top of the stack.
#    top() -- Get the top element.
#    getMin() -- Retrieve the minimum element in the stack.

class MinStack:
    def __init__(self):
        self.stack = []
        self.minstack = []
    
    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.stack.append(x)
        if not self.minstack or x <= self.minstack[-1]:
            self.minstack.append(x)

    # @return nothing
    def pop(self):
        num = self.stack.pop()
        if self.minstack and num == self.minstack[-1]:
            self.minstack.pop()

    # @return an integer
    def top(self):
        return self.stack[-1]

    # @return an integer
    def getMin(self):
        if self.minstack:
            return self.minstack[-1]
        return 0
