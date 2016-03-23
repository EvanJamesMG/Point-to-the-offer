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

输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
'''


class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if tinput == None or len(tinput) == 0 or k>len(tinput) or k==0:
            return []
        res = []
        tinput.sort()
        res = tinput[:k]
        return res


if __name__ == '__main__':
    res = Solution().GetLeastNumbers_Solution([1, 2, 3, 4, 5, 5], 4)
    print(res)
