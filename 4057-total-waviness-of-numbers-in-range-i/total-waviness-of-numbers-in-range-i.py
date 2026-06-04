class Solution(object):
    def totalWaviness(self, num1, num2):
        count=0
        for i in range (num1,num2+1):
            s=str(i)
            for j in range (1,len(s)-1):
                current=s[j]
                prev=s[j-1]
                upcom=s[j+1]
                if current>prev and current >upcom:
                    count+=1
                elif current<prev and current<upcom:
                    count+=1
        return count
            


        
        