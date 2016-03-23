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

求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？
为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,但是对于后面问题他就没辙了。
ACMer希望你们帮帮他,并把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数。
'''


class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        count = 0
        for item in range(1,n+1):
            pstr = str(item)
            count += pstr.count('1')
        return count
