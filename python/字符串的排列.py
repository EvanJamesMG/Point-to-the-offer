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

输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。 结果请按字母顺序输出。
输入描述:
输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。

递归，穷举全排列
'''
class Solution:
    def Permutation(self, ss):
        if ss == None or len(ss) == 0:
            return []
        if len(ss) == 1:
            return [ss]
        length = len(ss)
        res = []
        prenode = None
        for i in range(length):
            temlist = ss[i]
            if prenode == temlist:
                continue
            else:
                for sublist in self.Permutation(ss[:i] + ss[i + 1:]):
                    res.append(temlist + sublist)
            prenode = temlist
        return res


if __name__ == '__main__':
    res = Solution().Permutation('abc')
    print(res)
