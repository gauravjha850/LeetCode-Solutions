class Solution(object):
    def romanToInt(self, s):

        word_map={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        result=list(s)
        count=0
        for i in range (len(result)):

            
            
            
            current_value=word_map[result[i]]
            if i+1 < len(result) and current_value < word_map[result[i+1]]:

                count =count - current_value
            else:
                count=count+current_value

        return count



        