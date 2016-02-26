'''
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
实际也是斐波那契数列 <剑指offer> p77
'''
# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        res = [0]*(number+1)
        res[0]=1
        if number>=1:
        	res[1]=1
        if number >=2:
            res[2]=2
        if number >=3:
            for i in range(3,number+1):
                res[i] = res[i-1]+res[i-2]
        return res[number]
        
