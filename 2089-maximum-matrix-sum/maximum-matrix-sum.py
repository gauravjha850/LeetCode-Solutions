class Solution(object):
    def maxMatrixSum(self, matrix):
        neg=0
        sums=0
        min_abs_value=float('inf')
        for row in matrix:
            for val in row:
                sums=sums+abs(val)
                if val <0:
                    neg+=1
                if abs(val)< min_abs_value:
                    min_abs_value=abs(val)
        if neg%2!=0:
            return sums- (2*(min_abs_value))
        return sums


        
        