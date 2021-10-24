"""
Editor:Hyean
E-mail:1067065568@qq.com
"""
"""一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。"""


# def numways(n):
#     """
#     青蛙跳n级台阶的总跳法
#     :param n: 台阶总数
#     :return: 返回方法总数
#     """
#     dp = []
#     if n == 1:
#         dp.append(1)
#     elif n == 2:
#         dp.append(2)
#     else:
#         dp.append(dp[n-2] + dp[n-3])
#     return dp[n-1]
#
# print(numways(3))


def numWay2(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        a, b = 1, 2
        for i in range(3, n + 1):
            a, b = b, (a + b) % 1000000007
        return b


print(numWay2(4))
