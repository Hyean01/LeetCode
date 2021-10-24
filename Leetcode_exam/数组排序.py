"""
Editor:Hyean
E-mail:1067065568@qq.com
"""
"""对一个数组进行排序，按元素位数进行排序，先比较首位，首位相同比较第二位……例如：7，69，53——> 7>69>53"""


def arr_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr) - 1):
            if len(str(arr[j])) > len(str(arr[j + 1])):
                length = len(str(arr[j + 1]))
            else:
                length = len(str(arr[j]))
            for k in range(length):
                if str(arr[j])[k] == str(arr[j + 1])[k]:
                    continue
                elif str(arr[j])[k] > str(arr[j + 1])[k]:
                    break
                else:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    break
    return arr

li = [650, 6571, 730, 5444, 220, 912, 23, 231]
print(arr_sort(li))
