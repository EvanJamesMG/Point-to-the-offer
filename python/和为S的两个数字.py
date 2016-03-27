'''
题目描述

输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。 
输出描述:
对应每个测试案例，输出两个数，小的先输出。

利用hashmap
'''
# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        if array == None or len(array)==0:
            return []
        map = {}
        res = []
        for sub in array:
            map[sub] = 1
        for sub in array:
            if (tsum - sub) in map:
                if [sub, tsum - sub] not in res and tsum >= sub:
                    res.append([sub, tsum - sub])
        minfac = sys.maxint
        fres = []
        for sub in res:
            if sub[0] * sub[1] < minfac:
                minfac = sub[0] * sub[1]
                fres = [sub[0], sub[1]]
        return fres
