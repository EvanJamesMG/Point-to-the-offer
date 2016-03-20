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

输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。

解题思路：
后序遍历得到的序列中，最后一个数是树的根节点的值。数组中的前面的数字可以分为两个部分：
第一部分树左子树节点的值，它们都比根节点的值要小；
第二部分树右子树节点的值，它们都比根节点的值要大。

通过和根节点比较值大小，找出左右子树分界点的index,然后对左右子树分别递归。
'''
class Solution:
    def VerifySquenceOfBST(self, sequence):
        if sequence == None or len(sequence) == 0:
            return False
        length = len(sequence)
        root = sequence[-1]
        breakindex = 0
        while sequence[breakindex] < root and breakindex < length - 1:
            breakindex += 1

        for i in range(breakindex, length):
            if sequence[i] < root:
                return False

        left = True
        if breakindex > 0:
            left = self.VerifySquenceOfBST(sequence[:breakindex])
        right = True
        if breakindex < length - 1:
            right = self.VerifySquenceOfBST(sequence[breakindex:length-1])

        return left and right


