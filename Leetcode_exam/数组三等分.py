"""
Editor:Hyean
E-mail:1067065568@qq.com
"""


# [1,2,3,-1,0,1,4,-1,0]
# [1,2] [3,-1,0,1] [4,-1,0] = 3
# [1,2] [3] [-1,0,1,4,-1,0] = 3

# [1,2,4,3,-1,0,1,-1,0] = 9 --> True

# 当且仅当能够被切分成三等分的子数组时，返回True，其他情况返回False

# def canSplitThreeSubsets(lists:list) -> bool:
#     flag = 0
# 	for i in range(len(lists)):
# 		if sum(lists)/ sub_sum == 3:
# 			for j in lists[i:]:
# 				if lists[j]
#           flag = 1
#           break
#         else:
# 			sub_sum += i
#     if flag == 0:
# 		return False
#     else:
# 		return True


def canSplitThreeSubsets(lists):
    if sum(lists) % 3 != 0:  # 判断数组是否可以三等分
        return False
    else:
        sub_sum = sum(lists) / 3    # 求出数组三等分后子数组的和
        flag = 0
        start = 0      # 遍历的起始位置
        for i in range(len(lists)):
            if sum(lists[start:i]) == sub_sum:  # 如果起始位置到当前位置的子数组之和等于三等分子数组之和，那么当前就是一个子数组
                flag += 1   # 求到一个子数组，flag +1
                start = i  # 改变遍历的起始位置，继续寻找下一个子数组
        if flag == 3:  # 如果最后flag = 3 ， 那么就是获取了三个子数组了，满足要求，所以返回True
            return True
        else:
            return False


li = [1, 2, 4, 3, -1, 0, 1, -1, 0]

# print(canSplitThreeSubsets(li))


# print([x**2 for x in range(1, 10)])
#
# li_new = list(set(li))
# print(li_new)
import random
# print(random.randint(1, 100) + random.random(), random.randrange(1))
# randint包含右边界，randrange不包含右边界，实际rand就是调用的randrange


li_1 = [1, 2, 3, 4, 5]
new_nu = []
# 求可以组成多少个不含重复数字的三位数
for i in li_1:
    for j in li_1:
        for k in li_1:
            if i != j and j != k:
                new_nu.append(int("".join((str(i), str(j), str(k)))))
print(new_nu, len(new_nu))
