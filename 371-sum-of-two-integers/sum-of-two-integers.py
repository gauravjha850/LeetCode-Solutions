class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        mask=0xFFFFFFFF
        while b!=0:
            sum_without_carry=(a^b)& mask

            carry=((a&b) <<1 ) & mask
            a=sum_without_carry
            b=carry
        return a if a<=0x7FFFFFFF else ~(a ^ mask)

        