# coding=utf-8
import collections

__author__ = 'EvanJames'
'''
题目描述

在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。

请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

输入描述:
array： 待查找的二维数组
target：查找的数字


输出描述:
查找到返回true，查找不到返回false
'''


class Solution:
    # array 二维列表
    def Find(self, array, target):
        # write code here
        if array == None or len(array) == 0:
            return False
        h = 0
        l = len(array[0]) - 1
        while h <= len(array)-1 and l >= 0:
            if array[h][l] == target:
                return True
            elif array[h][l] > target:
                l -= 1
            else:
                h += 1
        return False


if __name__ == "__main__":
    result = Solution().Find([[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]], 11)
    print(result)
