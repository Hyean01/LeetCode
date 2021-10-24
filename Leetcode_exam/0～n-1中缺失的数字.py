"""
Editor:Hyean
E-mail:1067065568@qq.com
"""
"""一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。
在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。"""


def missingNum(nums):
    if nums[0] == 1:
        return 0
    else:
        flag = 0
        missingnum = 0
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] == 2:
                flag = 1
                missingnum = nums[i] + 1
        if flag:
            return missingnum
        else:
            return nums[-1] + 1
li = [0,1,2,3,5]


def missingnum(arry):
    """通过求和的方式，得出差值，差的就是缺的那一个数"""
    return sum(range(0, len(arry)+1)) - sum(arry)

print(missingnum(li))