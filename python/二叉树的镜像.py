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

操作给定的二叉树，将其变换为源二叉树的镜像。 
输入描述:
二叉树的镜像定义：源二叉树 
    	    8
    	   /  \
    	  6   10
    	 / \  / \
    	5  7 9 11
    	镜像二叉树
    	    8
    	   /  \
    	  10   6
    	 / \  / \
    	11 9 7  5
'''
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        if root:
            root.left, root.right = self.Mirror(root.right),self.Mirror(root.left)
            return root
