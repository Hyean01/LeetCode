"""
Editor:Hyean
E-mail:1067065568@qq.com
"""
def isOneBitCharacter(bits) -> bool:
        """
        第一种字符可以用一比特0来表示。第二种字符可以用两比特(10 或 11)来表示。现给一个由若干比特组成的字符串。
        问最后一个字符是否必定为一个一比特字符。给定的字符串总是由0结束。
        :param bits:给定的比特字符
        :return:最后一个是一个比特字符，返回TRUE，否则返回FALSE
        """
        # 思路一： 先判断倒数第二个字符，如果是0，那么直接输出FALSE，
        # 如果是1，则判断依次有偶数个1还是有奇数个1，如果是偶数，那么刚好为2比特字符，输出True如果为奇数，那就剩下一个1，与最后的0组成两比特字符，输出FALSE
        n = len(bits) -1
        i = 0
        while i < n:
            if bits[i] == 1:
                i += 2
            else:
                i += 1

        return i == n
print(isOneBitCharacter([1,1,0,1,0]))

