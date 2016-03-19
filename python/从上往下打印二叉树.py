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

从上往下打印出二叉树的每个节点，同层节点从左至右打印。
BFS 宽度优先搜索 注意队列出队 为 list.pop(0)
'''

class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        if root==None:
            return []
        res=[]
        temlist = []
        temlist.append(root)
        while temlist:
            length = len(temlist)
            for i in range(length):
                tem = temlist.pop(0)
                if tem.left:
                    temlist.append(tem.left)
                if tem.right:
                    temlist.append(tem.right)
                res.append(tem.val)
        return res
