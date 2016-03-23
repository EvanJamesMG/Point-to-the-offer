# coding=utf-8
import sys

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
HZ偶尔会拿些专业问题来忽悠那些非计算机专业的同学。今天测试组开完会后,他又发话了:在古老的一维模式识别中,
常常需要计算连续子向量的最大和,当向量全为正数的时候,问题很好解决。但是,如果向量中包含负数,是否应该包含某个负数,
并期望旁边的正数会弥补它呢？例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)。你会不会被他忽悠住？
'''


class Solution:
    def FindGreatestSumOfSubArray(self, array):
        if array == None or len(array) == 0:
            return None
        sumnum = -sys.maxint
        maxnum = -sys.maxint
        for i in range(len(array)):
            if sumnum < 0:
                sumnum = array[i]
            else:
                sumnum += array[i]
            if sumnum > maxnum:
                maxnum = sumnum
        return maxnum


if __name__ == '__main__':
    res = Solution().FindGreatestSumOfSubArray([1, 2, 3, 4, 5, 5])
    print(res)
