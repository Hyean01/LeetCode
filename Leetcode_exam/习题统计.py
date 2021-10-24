"""
Editor:Hyean
E-mail:1067065568@qq.com
"""
from functools import reduce


class Solution:
    def reverseList(self, head):
        """
        206. 给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
        :param head:
        :return:
        """
        pre, curr = None, head  # pre代表前面一个元素
        while curr:  # 当前节点为空的时候，就完成全部节点的反转了
            nxt = curr.next  # 先把下一个节点保存下来，以为第二轮需要用到
            curr.next = pre  # 修改当前这个节点的指向，之前curr.next是指向下一个节点的，要反转，所以curr.next的下一个节点应该要是他之前的结点，就是pre
            pre = curr  # 修改完成后，pre需要往后移一个位置，作为下一元素反转的前一个元素
            curr = nxt  # 当前这个节点完成反转后，需要把指针后移一个结点，把后面一个节点作为当前需要反转的节点了
        return pre  # pre走到最后一个节点，完成反转后，这最后一个节点就是链表的头节点，所以返回头节点即可返回整个反转后的链表     3#

    def singlenumber(self, nums):
        """
        136. 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
        :param nums:
        :return:
        """
        # re = nums[0]
        # for i in nums[1:]:
        #     re = re ^ i
        # return re

        return reduce(lambda x, y: x ^ y, nums)         # 通过lambda对列表元素做位运算
    """答案是使用位运算。对于这道题，可使用异或运算 。异或运算有以下三个性质。
任何数和 00 做异或运算，结果仍然是原来的数，即 a⊕0=a。
任何数和其自身做异或运算，结果是 00，即 a⊕a=0。
异或运算满足交换律和结合律，即a⊕b⊕a=b⊕a⊕a=b⊕(a⊕a)=b⊕0=b。"""

    def longestCommentprefix(self, nums):
        """
        14. 最长公共前缀:编写一个函数来查找字符串数组中的最长公共前缀。如果不存在公共前缀，返回空字符串 ""。
        :param nums:
        :return:
        """
        if not nums:
            return ""
        else:
            prefix = nums[0]
            curryprefix = nums[0]
            for temp in nums[1:]:
                lenght = min(len(curryprefix), len(temp))
                if not lenght:
                    return ""
                else:
                    for i in range(lenght):
                        if curryprefix[i] == temp[i] and i != (lenght-1):
                            continue
                        elif curryprefix[i] == temp[i] and i == (lenght-1):
                            curryprefix = curryprefix[:lenght]
                            prefix = curryprefix
                            break
                        else:
                            curryprefix = curryprefix[:i]
                            prefix = curryprefix
                            break
            return prefix

    def merge(self, nums1, nums2, m, n):
        """
        88. 合并两个有序数组
        :param nums1:
        :param nums2:
        :return:
        """
        nums1 = nums1[:m]
        nums1.extend((nums2[:n+1]))
        nums1.sort()
        return nums1

    def missingNum(nums):
        """
        一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。
        :return:
        """
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

    def reverseString(s):
        """
        编写一个函数，其作用是将输入的字符串反转过来。
        :return:
        """
        l, r = 0, len(s) - 1  # 用两个指针分别指向头尾元素，这样就可以直接交换，不用额外定义数组去存储
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return s

    def search4(arry, target):
        """使用二分法递归查找target和target-1的右边界，两个右边界的差值就是要找元素的数量"""
        def helper(tar):
            i, j = 0, len(arry) - 1
            while i <= j:
                m = (i + j) // 2
                if arry[m] <= tar:
                    i = m + 1
                else:
                    j = m - 1
            return i

        return helper(target) - helper(target - 1)

    def lengthOfLongestSubstring(s):
        """
        3. 无重复字符的最长子串
        :param s: 需要寻找的字符串
        :return: 最长子串的长度
        """
        currentsub = ""
        longestsub = ["0"]
        if len(s) == 0:
            return 0
        else:
            for i in s:
                if i not in currentsub:
                    currentsub += i
                    if len(currentsub) > len(longestsub[0]):
                        longestsub[0] = currentsub
                else:
                    currentsub = currentsub[currentsub.index(i) + 1:] + i

            return len(longestsub[0])

    def canSplitThreeSubsets(lists):
        if sum(lists) % 3 != 0:  # 判断数组是否可以三等分
            return False
        else:
            sub_sum = sum(lists) / 3  # 求出数组三等分后子数组的和
            flag = 0
            start = 0  # 遍历的起始位置
            for i in range(len(lists)):
                if sum(lists[start:i]) == sub_sum:  # 如果起始位置到当前位置的子数组之和等于三等分子数组之和，那么当前就是一个子数组
                    flag += 1  # 求到一个子数组，flag +1
                    start = i  # 改变遍历的起始位置，继续寻找下一个子数组
            if flag == 3:  # 如果最后flag = 3 ， 那么就是获取了三个子数组了，满足要求，所以返回True
                return True
            else:
                return False

    def numWay2(n):
        """
        一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。
        :return:
        """
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            a, b = 1, 2
            for i in range(3, n + 1):
                a, b = b, (a + b) % 1000000007
            return b

    def isValid1(s):
        """
        给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效
        使用栈结构存储左括号，依次遍历，遇到右括号就进行比较栈顶的左括号
        :param s:
        :return:
        """
        left = []
        if len(s) == 0:
            return True
        elif s[0] in [")", "]", "}"] or s[-1] in ["(", "[", "{"] or len(s) % 2 != 0:
            return False
        else:
            for i in range(len(s)):
                if s[i] in ["(", "[", "{"]:
                    if len(left) == len(s) / 2:
                        return False
                    else:
                        left.append(s[i])
                elif s[i] in [")", "]", "}"] and len(left) == 0:
                    return False
                elif len(left) > 0 and (s[i] == ")" and left[-1] == "(") or (s[i] == "]" and left[-1] == "[") or (
                        s[i] == "}" and left[-1] == "{"):
                    left.pop()
                    if len(left) == 0 and i == len(s) - 1:
                        return True
                    elif len(left) > 0 and i == len(s) - 1:
                        return False
                else:
                    return False

    def move_zero2(arry):
        """给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
        使用一个指针；来指向不为0的索引位置，遇到不为0的元素，就把它交换到指针所指的位置处"""
        j = 0
        for i in range(len(arry)):
            if arry[i] != 0:
                arry[j], arry[i] = arry[i], arry[j]
                j += 1
        return arry

    def arr_sort(arr):
        """
        对一个数组进行排序，按元素位数进行排序，先比较首位，首位相同比较第二位……例如：7，69，53——> 7>69>53
        :return:
        """
        for i in range(len(arr) - 1):
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

    def frequencySort(self, nums):
        
        """451. 根据字符出现频率排序"""
        dic = {}
        for i in nums:      # 遍历字符串，使用hash记录每个元素出现的频率
            if i in dic:
                dic[i] = dic[i] + 1
            else:
                dic[i] = 1
        dic_order = sorted(dic.items(), key=lambda x: x[1], reverse=False)  # 使用sorted函数排序，转换成list去排序
        newnums = ""
        for k, v in dic_order:
            newnums = newnums + k*v     # 然后Python中字符串乘以数字就是复制效果比如：'a' * 3 == 'aaa'

        return newnums

    def getIntersectionNode(self, headA, headB):
        """160. 相交链表.
        给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表没有交点，返回 null 。"""
        while headA and headB:
            pass
            



Test = Solution()
#
# li = [4,4,2,2,1,3,1,5,3,5,7]
# strs = ["ab", "a"]
# nums1 = [1,2,3,0,0,0]
# nums2 = [2,5,6]
print(Test.frequencySort("asdasdadasda"))

