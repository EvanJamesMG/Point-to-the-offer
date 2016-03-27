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

统计一个数字在排序数组中出现的次数
两种方法：二分查找；线性迭代；

'''


class Solution:
    def GetNumberOfK(self, data, k):
        ''' 二分查找'''
        if data ==None:
            return 0
        left = 0
        right = len(data)-1
        res = 0
        index = -1
        while left <= right:
            mid = (left + right) / 2
            if data[mid] > k:
                right = mid - 1
            elif data[mid] < k:
                left = mid + 1
            else:
                index = mid
                break
        if index != -1:
            for i in range(index, -1, -1):
                if data[i] == k:
                    res += 1
            for i in range(index + 1, len(data)):
                if data[i] == k:
                    res += 1
        return res

        ''' 线性迭代'''
        if data ==None:
            return 0
        num = 0
        for i in range(len(data)):
            if data[i] == k:
                num += 1
            if num>0 and data[i]!=k:
                break
        return num


if __name__ == '__main__':
    res = Solution().GetNumberOfK([1,2,3,3,3,3], 3)
    print(res)
