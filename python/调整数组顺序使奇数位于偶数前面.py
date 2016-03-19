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

输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于位于数组的后半部分，

并保证奇数和奇数，偶数和偶数之间的相对位置不变。


思路有两种：
1.空间换时间，最简单，需要定义额外的数组
2.时间换空间，在原数组中操作，类似于插入排序，遇到奇数就插到前面 时间复杂度 最好O(n) 最坏O(n^2) 空间复杂度O（1）
'''
# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        '''
        :type array: List[int]
        :rtype: List[int]
        '''
        if array ==None or len(array)==0:
            return array
        n = len(array)
        for i in range(n):
            if array[i] % 2 == 1:
                tem = array[i]
                index = i
                for j in range(i - 1, -1, -1):
                    if array[j] % 2 == 0:
                        array[j + 1] = array[j]
                        index = j
                    else:
                        break
                array[index] = tem
        return array
