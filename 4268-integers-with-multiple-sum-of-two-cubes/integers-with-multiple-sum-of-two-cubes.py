class Solution(object):
    def findGoodIntegers(self, n):
        def cube_root_binary(num):
            if num ==0:
                return 0
            if num ==1:
                return 1
            low=1
            high=num
            target=1
            while low <= high :
                mid=low+(high-low)//2
                cube=mid**3
                if cube ==num:
                    return mid
                elif cube < num :
                    target=mid
                    low=mid+1
                else:
                     
                    high=mid-1
            return target
        sum_count={}
        max_a=cube_root_binary(n//2)
        for a in range (1,max_a +1):
            max_b=cube_root_binary(n-a**3)
            for b in range (a,max_b+1):
                cube_sum= a**3 +b**3

                if cube_sum in sum_count :
                    sum_count[cube_sum]= sum_count[cube_sum] +1
                else:
                    sum_count[cube_sum]=1
        good_num=[]
        for key,value in sum_count.items():
            if value >= 2 :
                good_num.append(key)
            
        good_num.sort()
        return good_num



        