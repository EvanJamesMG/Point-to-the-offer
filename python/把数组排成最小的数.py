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
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。

排序思路：对于两个备选数字a和b，如果str(a) + str(b) < str(b) + str(a)，则a在b之前，否则b在a之前
按照此原则对原数组从大到小排序即可

时间复杂度O（nlogn）

易错样例：
Input:     [0,0]
Output:    "00"
Expected:  "0"

'''


class Solution:
    def PrintMinNumber(self, num):
        num = sorted([str(x) for x in num], cmp=self.compare)
        sb = ''
        for x in num:
            sb += str(x)
        if sb.replace('0', '') == '':
            return '0'
        return int(sb)

    def compare(self, a, b):
        return [1, -1][a + b < b + a]


if __name__ == '__main__':
    res = Solution().PrintMinNumber([23, 45, 232, 8, 545])
    print(res)
