"""
Editor:Hyean
E-mail:1067065568@qq.com
"""
"""给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
函数应该返回这两个下标值 index1 和 index2，返回的下标值（index1 和 index2）不是从零开始的。"""


def twosum1(arry, target):
    """暴力枚举：两重遍历，看得出的元素和是否等于目标值
    空间复杂度： O（1）
    时间复杂度：O（n**2）
    """
    for i in range(len(arry) - 1):
        for j in range(i + 1, len(arry)):
            if arry[i] + arry[j] == target:
                return [i + 1, j + 1]  # 返回的下标从1开始，那么都需要+1


li = [-1, 0, 2, 5, 7, 11]
print(twosum1(li, -1))


def twosum2(arry, target):
    """
    利用双指针和升序数列的特点，从两头往中间逼近目标值
    空间复杂度： O（1）
    时间复杂度：O（n）
    :param arry:
    :param target:
    :return:
    """
    left = 0
    right = len(arry) - 1
    while left < right:
        if arry[left] + arry[right] == target:
            return [left + 1, right + 1]  # 如果两个数的和等于目标值，那就直接返回left+1 和 right+1， +1是因为index从1开始
        elif arry[left] + arry[right] > target:
            right -= 1  # 如果大于目标值，说明右边的数偏大，应该再往前移（这是升序数组）
        elif arry[left] + arry[right] < target:
            left += 1  # 如果小于目标值，说明左边的值偏小，应该往前移
        else:
            return [-1, -1]  # 表明数组中没有两个数的和等于目标值


print(twosum2(li, 9))


def twosum3(numbers, target):
    """
    使用二分法查找， 先固定第一个数，然后target-number1 得到第二个数，利用二分法查找这第二个数
    空间复杂度： O（1）
    时间复杂度：O（nlogn）
    :param numbers:
    :param target:
    :return:
    """
    for i in range(len(numbers)):
        low, hight = i + 1, len(numbers) - 1  # 从number1右侧第一个数开始查找，一直到数组最后一个数
        while low <= hight:
            mid = (low + hight) // 2
            if numbers[mid] == (target - numbers[i]):
                return [i + 1, mid + 1]
            elif numbers[mid] > (target - numbers[i]):
                hight = mid - 1
            else:
                low = mid + 1
    return [-1, -1]     # 全部遍历完成都没找到符合条件的返回值，就返回[-1, -1]表示数组中不存在两个数的和等于目标值的


li2 = [-1, 0, 2, 5, 7, 11]
print(twosum3(li2, 9))
