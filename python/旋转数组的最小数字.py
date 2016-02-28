# coding=utf-8

__author__ = 'EvanJames'
'''
题目描述:
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减序列的一个旋转，输出旋转数组的最小元素。例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
'''
'''
解题思路：
和 《leetcode》033.Search in Rotated Sorted Array.py and 081.Search in Rotated Sorted Array类似
但是不同的是，这道题不是寻找某个特定的target，而是寻找最小的元素。而且此题需要把包含重复元素和起始未旋转状态的情况都包含进去。

'''

class Solution:
    def minNumberInRotateArray(self, rotateArray):
        """
        :type rotateArray: List[int]
        :rtype: int
        """
        if rotateArray == None or len(rotateArray) == 0:
            return -1
        if rotateArray[0] < rotateArray[-1]:#数组未进行旋转的情况（旋转后的数组中第一个元素总是大于等于最后一个元素 （eg:34512））
            return rotateArray[0]
        left = 0
        right = len(rotateArray) - 1
        while left <= right:
            if right - left == 1: #结束状态，此时两指针的距离为1，左指针指向第一个递增子数组的结尾，右指针指向第二个递增字数组的开始
                mid = right
                break
            mid = (left + right) / 2

            if rotateArray[mid] == rotateArray[left] == rotateArray[right]:#当出现左中右三个指针指向的元素相同的情况时，无法判断中间指针位于前后哪一段，只能进行顺序查找
                return self.ordersearch(rotateArray, left, right)

            if rotateArray[left] <= rotateArray[mid]:#此时中间指针指向左递增子数组中元素，目标值在右递增字数组的第一个，因此令左指针项向右缩进
                left = mid
            else:#此时中间指针指向右递增子数组中元素，目标值在右递增字数组的第一个，因此令右指针项向左缩进
                right = mid
        return rotateArray[mid]

    def ordersearch(self, A, left, right):
        res = A[left]
        for i in range(left, right + 1):
            res = min(res, A[i])
        return res


if __name__ == "__main__":
    result = Solution().minNumberInRotateArray([1, 2, 3, 4, 5])
    print(result)
