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


class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


'''
题目描述

输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。

'''

class Solution:
    def TreeDepth(self, pRoot):
        if pRoot==None:
            return 0
        return max(self.TreeDepth(pRoot.left),self.TreeDepth(pRoot.right))+1
