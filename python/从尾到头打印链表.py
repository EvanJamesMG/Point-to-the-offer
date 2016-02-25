__author__ = 'EvanJames'
'''
字符串翻转 这个题返回的是一个新的列表，而不是表头
'''

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        if listNode:
            pre = None
            head = listNode
            res = []
            while head:
                tem = head.next
                head.next = pre
                pre = head
                head = tem
            while pre:
                res.append(pre.val)
                pre = pre.next
            return res
        else:
            return []


if __name__ == "__main__":
    result = Solution().printListFromTailToHead("")
    print(result)
