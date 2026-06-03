class Solution(object):
    def brokenCalc(self, startValue, target):
        count=0
        while startValue<target:
            if target%2==1:
                target+=1
                count+=1
            else:
                target//=2
                count+=1
        return count + (startValue- target )

        
        