# coding=utf-8

__author__ = 'EvanJames'
'''
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项。

斐波拉切数列是这样一个数列：1、1、2、3、5、8、13、21、……在数学上，其被以递归的方法定义：F0=0，F1=1，Fn=F(n-1)+F(n-2)（n>=2）
'''

class Solution:
    def Fibonacci(self, n):
        res = [0]*(n+1)
        res[0] = 1
        if n >=1:
            res[1] = 1
        if n >=2:
            res[2] =1
        if n>=3:
            for i in range(3,n+1):
                res[i] = res[i-1]+res[i-2]
        return res[n]



if __name__ == "__main__":
    result = Solution().Fibonacci(5)
    print(result)
