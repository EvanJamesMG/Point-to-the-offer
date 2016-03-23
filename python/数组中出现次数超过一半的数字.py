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
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。

此题和leetcode中不同的地方就是数组中不一定存在超过数组长度一半的元素，所以这里用hashmap做了元素个数的统计，之后判断。
'''
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        if numbers == None or len(numbers) == 0:
            return 0
        map = {}
        length = len(numbers)
        for i in range(length):
            if numbers[i] in map:
                map[numbers[i]] += 1
            else:
                map[numbers[i]] = 1
            if map[numbers[i]] > length / 2:
                return numbers[i]
        return 0


if __name__ == '__main__':
    res = Solution().MoreThanHalfNum_Solution([1, 2, 3, 4, 5, 5])
    print(res)
