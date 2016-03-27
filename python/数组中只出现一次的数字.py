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

一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
利用haspmap

'''


class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        if array == None or len(array) <= 1:
            return [0, 0]
        map = {}
        res = []
        for i in range(len(array)):
            if array[i] in map:
                map.pop(array[i])
            else:
                map[array[i]] = 1
        for i in map:
            res.append(i)
        return res


if __name__ == '__main__':
    res = Solution().FindNumsAppearOnce([1, 2, 3, 3, 2, 4])
    print(res)
