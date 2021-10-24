"""
Editor:Hyean
E-mail:1067065568@qq.com
"""
"""给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
"""
"""使用栈结构，如果是左括号，先存储，如果是右括号，那么就与之最近的一个左括号匹配，如果可以匹配上，那就移除该左括号，直到左括号为空，返回"""


def isValid1(s):
    """
    使用栈结构存储左括号，依次遍历，遇到右括号就进行比较栈顶的左括号
    :param s:
    :return:
    """
    left = []
    if len(s) == 0:
        return True
    elif s[0] in [")", "]", "}"] or s[-1] in ["(", "[", "{"] or len(s) % 2 !=0:
        return False
    else:
        for i in range(len(s)):
            if s[i] in ["(", "[", "{"]:
                if len(left) == len(s)/2:
                    return False
                else:
                    left.append(s[i])
            elif s[i] in [")", "]", "}"] and len(left) == 0:
                return False
            elif len(left) > 0 and (s[i] == ")" and left[-1] == "(") or (s[i] == "]" and left[-1] == "[") or (
                        s[i] == "}" and left[-1] == "{"):
                left.pop()
                if len(left) == 0 and i == len(s)-1:
                    return True
                elif len(left) > 0 and i == len(s)-1:
                    return False
            else:
                return False

s = "()))"
print(isValid1(s))


def isValid2(s):
    """
    通过替换的方式
    :param s:
    :return: 最后s为空，说明所有括号都有一一对应，如果不为空，说明不能完全配对
    """
    for i in range(len(s)):
        if "()" in s:
            s = s.replace("()", "")
        elif "[]" in s:
            s = s.replace("[]", "")
        elif "{}" in s:
            s = s.replace("{}", "")
    return not s


def isValid3(s):
    """
    通过栈结构存储左括号， 利用哈希映射存储每一种括号
    :param s:
    :return:
    """
    left = []
    dic = {")": "(", "]": "[", "}": "{"}
    if len(s) == 0: return True
    if len(s) % 2 != 0 or s[0] in ")]}" or s[-1] in "([{": return False
    for i in s:
        if i in dic:    # 默认是比对字典的键名，即i 是否在dic.key()里面
            if not left or left[-1] != dic[i]:
                return False
            left.pop()
        else:
            left.append(i)
    return not left


def isValid4(s):
    """
    通过栈存储右括号，遍历字符串的时候，遇到左括号，就相应的把右括号添加到栈里；遇到右括号，就取出栈顶的元素进行比较，如果不一致或者栈为空，那么就是FALSE
    :param s:
    :return:
    """
    left = []
    if len(s) == 0: return True
    if len(s) % 2 != 0 or s[0] in ")]}" or s[-1] in "([{": return False
    for i in s:
        if i == "(":
            left.append(")")
        elif i == "[":
            left.append("]")
        elif i == "{":
            left.append("}")
        elif len(left) == 0 or left.pop() != i:
            return False
    return not left


s = "([()])"
print(isValid4(s))
