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

输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
就是转圈
'''

# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):

        if matrix==None or len(matrix)==0:
            return []
        res = []
        order = 0
        up = 0
        down = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        while up <= down and left <= right:

            if order == 0:
                for i in range(left, right + 1):
                    res.append(matrix[up][i])
                up += 1
            if order == 1:
                for i in range(up, down + 1):
                    res.append(matrix[i][right])
                right -= 1
            if order == 2:
                for i in range(right, left - 1, -1):
                    res.append(matrix[down][i])
                down -= 1
            if order == 3:
                for i in range(down, up - 1, -1):
                    res.append(matrix[i][left])
                left += 1

            order = (order + 1) % 4
        return res
        
if __name__ == "__main__":
    result = Solution().printMatrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
    print(result)
