"""
Editor：Hyean.qin
E-mail: 1067865568@qq.com
Type: Python24
Time: 2021/9/6 16:38
"""
from functools import reduce


class LeetCode:
    def reversechain(self, head):
        """
        206. 反转链表
        :param head:
        :return:
        """
        while cur:
            prev, cur = None, head
            temp = cur.next  # 先保存下一个节点
            cur.next = prev  # 把当前节点指向反转
            prev = cur  # 把之前的节点后移，继续下一轮
            cur = temp
        return prev

    def SingleNumber(self, nums):
        """
        136. 只出现一次的数字:给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
        :param nums:
        :return:
        """
        return reduce(lambda x, y: x ^ y, nums)  # 使用异或运算，可以得出只出现一次的数字

    def longestCommonPrefix(self, number):
        """
        14. 最长公共前缀:查找字符串数组中的最长公共前缀
        :param number:
        :return:
        """
        curfix = number[0]
        for item in number[1:]:
            lenght = min(len(curfix), len(item))
            for i in range(lenght):
                if curfix[i] == item[i] and i != lenght - 1:
                    continue
                elif curfix[i] == item[i] and i == lenght - 1:  # 考虑到最后一个元素也相等，这时候也要更新当前字串
                    curfix = curfix[:i + 1]
                    break
                else:
                    curfix = curfix[:i]
                    break
        if curfix:
            return curfix
        else:
            return ""

    def merge(self, nums1, nums2, m, n):
        """
        88. 合并两个有序数组
        :param num1：数组1
        :param num2:数组2
        :param m:数组1中有效元素的长度
        :param n:数组2中有效元素的长度
        :return:
        """
        p1, p2 = m - 1, n - 1
        tail = m + n - 1
        while p2 >= 0 and p1 >= 0:
            if nums2[p2] >= nums1[p1]:  # 如果数组2的元素大于等于数组1的元素，那么就是把数组2的元素放到tail指针的位置，然后tail指针往前移动，指向数组2的指针p2也往前移动，指向新的元素
                nums1[tail] = nums2[p2]
                tail -= 1
                p2 -= 1
            elif nums2[p2] < nums1[p1]:  # 如果数组2的元素小于数组1的元素，那么就是把数组1的这个元素放到tail指针的位置，tail指针和指向数组1的p1指针同时往前移动
                nums1[tail] = nums1[p1]
                tail -= 1
                p1 -= 1
        if p2 >= 0:  # 如果nums2有剩余元素未遍历完，则说明剩余元素都是比num1元素小的，把剩余元素整体搬到num1上即可
            nums1[:p2 + 1] = nums2[:p2 + 1]
        return nums1

    def climbStairs(self, n):
        """
        70. 爬楼梯: 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
        :param n:
        :return:
        """
        # d0, d1, temp = 1, 2, 0
        # if n <= 2:
        #     return n
        # for i in range(3, n+1):
        #     temp = d1
        #     d1 = d0 + d1
        #     d0 = temp
        # return d1

        a, b = 1, 1
        for i in range(n - 1):
            a, b = b, a + b
        return b

    def missingNumber(self, nums):
        """
        268. 丢失的数字:给定一个包含 [0, n] 中 n 个数的数组 nums ，找出 [0, n] 这个范围内没有出现在数组中的那个数。
        :param nums:
        :return:
        """
        # return sum(range(len(nums) + 1)) - sum(nums)  # 数学方法，range（0，n+1）的和再减去数组的和，就是缺失的数字

        nums.sort()
        for index, value in enumerate(nums):    # 位运算，先把数组排序，然后用下标和值做位运算，因为下标和值刚好是一一对应的，
                                                # 如果对不上，那就是说那个索引的值改变了，原本位置应该是index的，所以缺少的值就是index
            if index ^ value != 0:
                return index
            elif index == len(nums) - 1:
                return index + 1

    def twosum(self, nums, target):
        """
        1. 两数之和:给定一个整数数组 nums 和一个整数目标值 target,请你在该数组中找出和为目标值 target 的那两个整数，并返回它们的数组下标。
        :param nums:
        :param target:
        :return:
        """
        dic = {}
        for k, v in enumerate(nums):
            if target-v in dic:
                return [dic[target-v], k]
            else:
                dic[v] = k
        return []

    def search(self, nums, target):
        """
        704. 二分查找:给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。
        :param nums:
        :param target:
        :return:
        """
        low, high = 0, len(nums)-1
        while low <= high:
            mid = low + (high-low)//2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                low = mid + 1
            elif target < nums[mid]:
                high = mid - 1
        return -1

    def fib(self, n):
        """
        剑指 Offer 10- I. 斐波那契数列:写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项（即 F(N)）。斐波那契数列的定义如下:
        F(0) = 0,   F(1) = 1
        F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
        :param n:
        :return:
        """
        # a, b = 0, 1
        # for i in range(2, n+1):       # 数学交换的方式
        #     a, b = b, a + b
        #
        # return b % 1000000007

        dp = [0, 1]
        for i in range(2, n+1):     # 基于列表-动态规划的方式
            dt = dp[i-2] + dp[i-1]
            dp.append(dt % 1000000007)

        return dp[n]

    def searchrange(self, nums, target):
        """
        34. 在排序数组中查找元素的第一个和最后一个位置:
        给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。如果数组中不存在目标值 target，返回 [-1, -1]。
        :param nums:
        :param target:
        :return:
        """
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low)//2
            if nums[mid] == target:     # 二分法找到目标值后， 左边界右边界分别向中间值逼近，直到左右边界值都与目标值相等
                if nums[low] == target and nums[high] == target:
                    return [low, high]
                elif nums[low] != target:   # 左边界不等于目标值，就继续往右移动，直到等于目标值
                    low += 1
                elif nums[high] != target:  # 右边界不等于目标值，就继续往左移动，直到等于目标值
                    high -= 1
            elif nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
        return [-1, -1]

    def sortArry(self, nums):
        """
        912. 排序数组:给你一个整数数组 nums，请你将该数组升序排列。
        :param nums:
        :return:
        """
        if len(nums) < 2:
            return nums
        else:
            lower = []
            higher = []
            for number in nums[1:]:
                if number < nums[0]:
                    lower.append(number)
                else:
                    higher.append(number)
            return self.sortArry(lower) + [nums[0]] + self.sortArry(higher)


if __name__ == '__main__':
    s = LeetCode()
    # print(s.fib(45))
    print(s.sortArry([1,4,2,3,6,9,3,5,1]))


