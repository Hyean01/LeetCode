"""
Editor:Hyean
E-mail:1067065568@qq.com
"""


def findstr(s):
    """
    给定一个字符串，找出不含有重复字符的最长子串的长度: 给定一个字符串，找出不含有重复字符的最长子串的长度
    :param s: 需要寻找的字符串
    :return: 最长子串的长度
    """
    sub_s = ""
    res = ["0"]
    if len(s) == 0:
        return 0
    else:
        for i in s:
            if i not in sub_s:
                sub_s += i
                if len(sub_s) > len(res[0]):
                    res[0] = sub_s
            else:
                sub_s = sub_s[sub_s.index(i)+1:] + i

        return len(res[0])


# print(findstr("fiwfowr"))


import unittest
from ddt import ddt, data

#读取用例数据
with open(r"E:\Py24\Leetcode_exam\testdata.txt", "r") as f:
    case_data = []
    for i in f.readlines():
        case_data.append(i.strip("\n"))


@ddt
class Test(unittest.TestCase):
    @data(*case_data)
    def test_01(self, case):
        print(self.assertEqual(int(case.split(",")[1]), findstr(case.split(",")[0])))


if __name__ == '__main__':
    unittest.main()
