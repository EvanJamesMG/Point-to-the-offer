'''
给定有序数组，里面包含正数或者负数或者0，返回数组中绝对值最小的数，不能用顺序查找
例子：-9，-6，-5，-1, 3, 5, 6, 7
返回-1
'''

class Solution:
    def getabsmin(self, list):
        if list == None or len(list) == 0:
            return
        length = len(list)
        left = 0
        right = length - 1
        while left <= right:
            mid = (left + right) / 2
            if list[mid] == 0:
                return 0
            elif list[mid] > 0:
                if list[mid - 1] == 0:
                    return 0
                elif list[mid - 1] > 0:
                    right = mid
                else:
                    if cmp(abs(list[mid - 1]), list[mid]) < 0:
                        return list[mid - 1]
                    else:
                        return list[mid]
            else:
                if list[mid + 1] == 0:
                    return 0
                elif list[mid + 1] < 0:
                    left = mid
                else:
                    if cmp(abs(list[mid]), list[mid + 1]) < 0:
                        return list[mid]
                    else:
                        return list[mid + 1]


if __name__ == '__main__':
    res = Solution().getabsmin([-7, -5, -3, 2, 3, 6, 7])
    print(res)
