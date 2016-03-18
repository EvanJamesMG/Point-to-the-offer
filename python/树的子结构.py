# coding=utf-8
__author__ = 'EvanJames'

# -*- coding:utf-8 -*-
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

输入两颗二叉树A，B，判断B是不是A的子结构。

上述代码中，我们递归调用HasSubtree遍历二叉树A,如果发现某一节点的值和树B的头结点值相同，则调用ispartof做第二步的判断
第二步是判断数A中以R为结点的子树是不是和树B具有相同的结构。同样我们以递归的思想来考虑：如果结点R的值和树B的根节点的值不相同，
则以R为根节点的子树和树B肯定不具有相同的节点；如果他们的值相同，则递归地判断它们各自的左右节点的值是不是相同。递归结束的条件是
我们达到了树A或者树B的叶节点。
'''

class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        if pRoot1 and pRoot2:
            if pRoot1.val == pRoot2.val:
                res = self.ispartof(pRoot1, pRoot2)
            if res == False:
                res = self.HasSubtree(pRoot1.left, pRoot2)
            if res == False:
                res = self.HasSubtree(pRoot1.right, pRoot2)
        return res

    def ispartof(self, pRoot1, pRoot2):
        if pRoot2 == None:
            return True
        if pRoot1 == None:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return self.ispartof(pRoot1.left, pRoot2.left) and self.ispartof(pRoot1.right, pRoot2.right)
