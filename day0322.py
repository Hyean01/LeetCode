#!/usr/bin/env python 
# -- coding:utf-8 -- 
# hyean.qin@gmail.com

"""给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。"""
# 二分法查找目标值
def searchInsert(numlist, num):
    left, right = 0, len(numlist)
    while (left < right):
        mid = int(left + (right-left)/2)
        if numlist[mid] >= num:
            right = mid
        else:
            left = mid + 1

    return left

def isBadVersion(n):
    if n >= 5:
        return True
    else:
        return False
def firstbadversion(n):
    left, right = 1, n
    while (left < right):
        mid = int(left + (right-left)/2)
        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1

    return left


if __name__ == '__main__':
    res = searchInsert([1,2,5,6,8], 7)
    print(firstbadversion(19))
