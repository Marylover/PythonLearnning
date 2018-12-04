import re
import math
class Solution:
    def myAtoi(self,str):
        re_num = re.compile(r'^\s*(\+?\-?\d+)\D*')
        try:
            num = int(re_num.match("+-2").groups()[0])
            if abs(num) >= pow(2,31) and num > 0:
                num =  2147483647
            elif abs(num) >= pow(2,31) and num < 0:
                num = -2147483648
        except :
            num = 0
        print(num)
