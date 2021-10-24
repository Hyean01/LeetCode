"""
Editor:Hyean
E-mail:1067065568@qq.com
"""
"""给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。"""
"""
1. 使用一个新数组，遍历原数组，遇到非零的直接添加到数组，最后补全0
2. 使用指针，遇到非0的，插入指针处，指针后移
3. 使用双指针，head指针代表非0.tail指针代表0，遇到非0的，移到head指针索引处，head指针往后移，tail指针同理
4. 先统计数组中的0的数量，然后删除全部的0，再再删除后的数组最后补上相同位数的0
"""


def move_zero1(arry):
    """使用两个新的数组，一个存放非0元素，一个存放是0的元素，最后组合返回"""
    arr_new = []
    arr_zero = []
    for i in arry:
        if i != 0:
            arr_new.append(i)
        else:
            arr_zero.append(i)
    arr_new.extend(arr_zero)
    return arr_new


def move_zero2(arry):
    """使用一个指针；来指向不为0的索引位置，遇到不为0的元素，就把它交换到指针所指的位置处"""
    j = 0
    for i in range(len(arry)):
        if arry[i] != 0:
            arry[j], arry[i] = arry[i], arry[j]
            j += 1
    return arry


def move_zero4(arry):
    """
    :type arry: object
    """
    # zero_num = arry.count(0)
    # while 0 in arry:
    #     arry.remove(0)
    # for i in range(zero_num):
    #     arry.append(0)
    # return arry
    index_zero = 0
    for i in range(len(arry)):
        index = i-index_zero
        if arry[index] == 0:
            arry.pop(index)
            arry.append(0)
            index_zero += 1
    return arry


li = [9, 0, 0, 3, 12]
print(move_zero4(li))



