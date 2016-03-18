# coding=utf-8

__author__ = 'EvanJames'


# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


'''
字符串翻转，没难度
'''


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        pre = None
        head = pHead
        while head:
            tem = head.next
            head.next = pre
            pre = head
            head = tem
        return pre
