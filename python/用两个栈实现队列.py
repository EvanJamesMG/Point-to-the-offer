'''
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
'''


class Solution:
    def __init__(self):
        self.inStack = []
        self.outStack = []
    def push(self, node):
        self.inStack.append(node)
    def pop(self):
        if self.outStack:
            return self.outStack.pop()
        else:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
            return self.outStack.pop()
