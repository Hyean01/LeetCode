"""
Editor:Hyean
E-mail:1067065568@qq.com
"""
"""统计一个数字在排序数组中出现的次数。"""


def search1(arry, target):
    """
    直接使用count函数
    :param list:
    :param target:
    :return:
    """
    return arry.count(target)


li = [0, 1, 1]
print(search1(arry=li, target=1))

from collections import Counter


def search2(arry, target):
    """
    使用collection里面的Counter函数,Counter(arry)统计每个元素出现的次数，再通过。get()函数取出指定元素出现的次数
    :param arry:
    :param target:
    :return:
    """
    if Counter(arry).get(target):
        return Counter(arry).get(target)
    else:
        return 0


print(search2(li, 2))


def search3(arry, target):
    """
    通过遍历计数得出指定元素的值
    :param arry:
    :param target:
    :return:
    """
    count = 0
    for i in arry:
        if i == target:
            count += 1

    return count


print(search3(li, 1))


def search4(arry, target):
    """使用二分法递归查找target和target-1的右边界，两个右边界的差值就是要找元素的数量"""

    def helper(tar):
        i, j = 0, len(arry) - 1
        while i <= j:
            m = (i + j) // 2
            if arry[m] <= tar:
                i = m + 1
            else:
                j = m - 1
        return i

    return helper(target) - helper(target - 1)


print(search4(li, 1))
