# -*- coding:utf-8 -*-
'''
题目描述

将一个字符串转换成一个整数，要求不能使用字符串转换整数的库函数。
注意特殊情况：
比方说正负号问题：“-432432”，还有字符串内部含有其他符号“43dr24”(这时返回0)
'''
class Solution:
    def StrToInt(self, s):
        if s==None or len(s)==0:
            return 0
        tem = 0
        for i in range(len(s)):
            if s[i]>='0' and s[i]<='9':
                tem =tem*10+int(s[i])
            else:
                if i!=0:
                    return 0
        if s[0]=='-':
            return -tem
        else:
            return tem
