"""
Editor:Hyean
E-mail:1067065568@qq.com
"""
"""输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。为简单起见，标点符号和普通字母一样处理。
例如输入字符串"I am a student. "，则输出"student. a am I"。
输入: "  hello world!  "
输出: "world! hello"
解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。

输入: "a good   example"
输出: "example good a"
解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
"""

#
# def reverseword(String: str):
#     return " ".join(String.strip(" ").split(" ").reverse())


String = " a good   example  "
l = String.strip().split()
l.reverse()
print(" ".join(l))

# split() 会根据空格进行切割，中间无论有多少个空格，都会当做一个空格处理；但是如果写成split(" "),那么就会只按一个空格去切割
print(String.split())
print(String.split(" "))    # 这样子切割后得到的数组中会包含中间的空格，当中间有多个空格的时候
