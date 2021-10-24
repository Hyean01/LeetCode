"""
Editor:Hyean
E-mail:1067065568@qq.com
"""


def findRepeatNum1(arry):
    """直接遍历原数组，通过count函数---但是时间复杂度高，会超时"""
    for i in arry:
        if arry.count(i) > 1:
            return i


def findRepeatNum2(arry):
    """用一个新数组存储遍历过的元素"""
    arry_new = []
    for i in arry:
        if i not in arry_new:
            arry_new.append(i)
        else:
            return i


def findRepeatNum3(arry):
    """通过集合去重, 再遍历数组，比较两个数组同一索引位置的值是否相等，如果不相等，说明原本这个索引位置的值重复量，被set去重了"""
    arry_new = list(set(arry))
    for i in range(len(arry)):
        if i >= len(arry_new) or arry[i] != arry_new[i]:
            return arry[i]


# def findRepeatNum4(arry):
#     """通过集合去重, 新建一个空集合，通过遍历原数组往集合中添加元素，比较添加后集合长度是否改变，如果添加后没变，那当前这个元素就是重复元素"""
#     arry_new = ()
#     for i in arry:
#         curren_l = len(arry_new)
#         arry_new.__add__((i,))
#         print(arry_new)
#         if len(arry_new) == curren_l:
#             return i


from collections import Counter


def findRepeatNum5(arry):
    """通过Counter方法，得出每个元素的出现次数,collections.Counter(nums).most_common(K) 常用来获取数组和字符串中最大的TopK
    most_commom()返回的是列表嵌套元组的形式，Counter后是按元素出现次数从大到小排序的，所以取第一个就好，然后一个元组里第一个元素就是重复次数最多的元素"""
    return Counter(arry).most_common()[0][0]


print(findRepeatNum5([1, 2, 3, 5, 2, 2, 1, 5, 1]))
