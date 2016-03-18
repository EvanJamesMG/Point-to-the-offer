# coding=utf-8

__author__ = 'EvanJames'
'''
题目描述

输入一个链表，输出该链表中倒数第k个结点。
'''

# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

'''
考虑特殊情况：
1.链表为空
2.k的大小超过链表的长度
3.返回的是节点，不是节点的值
'''
class Solution:
    def FindKthToTail(self, head, k):
        if head == None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        p1 = p2 = dummy

        for i in range(k):
            p2 = p2.next
            if p2 == None:
                return None

        while p2:
            p1 = p1.next
            p2 = p2.next
        return p1
