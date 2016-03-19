# coding=utf-8
__author__ = 'EvanJames'
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
题目描述

定义栈的数据结构，请在该类型中实现一个能够得到栈最小元素的min函数。
思路：
开辟两个栈，一个栈是普通的栈，一个栈用来维护最小值的队列。
'''

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, node):
        self.stack.append(node)
        if len(self.minstack) == 0 or node < self.minstack[-1]:
            self.minstack.append(node)

    def pop(self):
        tem = self.stack.pop()
        if len(self.minstack) != 0 and tem == self.minstack[-1]:
            self.minstack.pop()

    def top(self):
        return self.stack[-1]

    def min(self):
        return self.minstack[-1]
