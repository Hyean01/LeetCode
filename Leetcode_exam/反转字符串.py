"""
Editor:Hyean
E-mail:1067065568@qq.com
"""
"""
编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。
不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。
"""


def reverseString(s):
    l, r = 0, len(s) - 1    # 用两个指针分别指向头尾元素，这样就可以直接交换，不用额外定义数组去存储
    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1
    return s


# print(reverseString(input().split(",")))

print(input()[::-1])

if __name__ == "__main__":
    pass

    

