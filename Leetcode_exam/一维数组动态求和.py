"""
Editor:Hyean
E-mail:1067065568@qq.com
"""
"""给你一个数组 nums 。数组「动态和」的计算公式为：runningSum[i] = sum(nums[0]…nums[i]) 。请返回 nums 的动态和。
输入：nums = [1,2,3,4]
输出：[1,3,6,10]
解释：动态和计算过程为 [1, 1+2, 1+2+3, 1+2+3+4] 。
"""


def runningsum(arr: list):
    for i in range(1, len(arr)):
        arr[i] = int(arr[i]) + int(arr[i-1])
    return arr


li = [1,2,3,4]
print(runningsum(li))