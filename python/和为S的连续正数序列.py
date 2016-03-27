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

    def TreeDepth(self, pRoot):
        if pRoot == None:
            return 0
        return max(self.TreeDepth(pRoot.left), self.TreeDepth(pRoot.right)) + 1


'''
题目描述

小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。
但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。
现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? Good Luck!

输出描述:
输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序

滑动窗口 [left, right] 初始大小为0，滑动的规则如下：

若元素之和 < s，窗口右边沿向右延伸，直到 元素之和≥s 为止。
若元素之和 > s，更新最小长度。然后窗口左边沿右移一位（即移除窗口中第一个元素），重复第1步
若元素之和 = s, 左右窗口同时右移一位。

'''


class Solution:
    def FindContinuousSequence(self, tsum):
        res = []

        if tsum == None or tsum <= 1:
            return []
        length = tsum/2+1
        list = [i+1 for i in range(length)]
        left, right = 0, 0
        while left <= right and left <= length and right <= length:
            if sum(list[left:right+1]) < tsum:
                right += 1
            elif sum(list[left:right+1]) > tsum:
                left += 1
            else:
                res.append(list[left:right + 1])
                left += 1
                right += 1
        return res
