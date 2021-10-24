"""
Editor:Hyean
E-mail:1067065568@qq.com
"""

"""给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
"""


def findNo(arry, target):
    """
    :param arry:原始需要寻找的数组
    :param target:目标值，两个数相加等于这个目标值
    :return:返回字典形式，每一个键值对就是对应的索引
    """
    dic = {}
    for i in range(len(arry)-1):
        for j in range(i+1, len(arry)):
            if int(arry[i]) + int(arry[j]) == target and i not in dic.keys() and i not in dic.values():
                dic[i] = j
    return dic


def two_sum(arry, target):
    data = []
    for i in range(len(arry)):
        num = target - arry[i]
        if num in arry[i:] and arry.index(num) not in data:
            data.extend([i, arry.index(num)])
            # data.append((i, arry.index(num)))
    return data


lis = [2, 7, 3, 9, 6, 5, 1, 4, 5, 4]
print(two_sum(lis, 9))
print(findNo(lis, 9))
