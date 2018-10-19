#leetcode 题解，这是一道正则匹配的问题，注意匹配的条件和异常情况
import re  
class Solution:
    def myAtoi(self,str):
        #匹配条件：以空格，数字或'+''-'开头，提取子列条件：包括正负号和数字
        #要保证提后紧跟着子列的字符串不含数字
        re_num = re.compile(r'^\s*(\+?\-?\d+)\D*')
        try:
            num = int(re_num.match(str).groups()[0])
            #注意题目要求的整数范围
            if abs(num) >= pow(2,31) and num > 0:
                num =  2147483647
            elif abs(num) >= pow(2,31) and num < 0:
                num = -2147483648
            else:
                return num
            #异常情况：不匹配或者无法用int()函数转为整形，例如（+-2）
        except :
            num = 0
        return num
    