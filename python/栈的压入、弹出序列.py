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

输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。假设压入栈的所有数字均不相等。
例如序列1,2,3,4,5是某栈的压入顺序，序列4，5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。

很巧妙的一种解法，另外开辟一个数组，依次存放的是入栈的元素，存放的同时找出第一个出栈的元素，确定出栈了几个元素，然后再继续入栈
最后如果和出栈列表中元素相同的话，最后新开辟的数组中不会再剩余元素。
'''


# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        if pushV == None or len(pushV) == 0:
            return False
        stack = []
        j = 0
        for i in range(len(pushV)):
            stack.append(pushV[i])
            while j < len(popV) and stack[-1] == popV[j]:
                stack.pop()
                j += 1
        return len(stack) == 0
