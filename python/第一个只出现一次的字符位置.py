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

在一个字符串(1<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符的位置。若为空串，返回-1。位置索引从0开始

先统计每个字符的个数，然后从字符串中依次遍历找出map中的统计数为1的字符。hashmap中查找元素时间复杂度为O(1)
'''


class Solution:
    def FirstNotRepeatingChar(self, s):
        if s == None or len(s) == 0:
            return -1
        map = {}
        for i in range(len(s)):
            if s[i] in map:
                map[s[i]] += 1
            else:
                map[s[i]] = 1
        for i in range(len(s)):
            if map[s[i]] == 1:
                return i
        return -1


if __name__ == '__main__':
    res = Solution().FirstNotRepeatingChar('aabccdbd')
    print(res)
