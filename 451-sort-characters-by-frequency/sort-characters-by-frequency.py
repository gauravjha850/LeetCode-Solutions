class Solution(object):
    def frequencySort(self, s):
        counts= {}
        for char in s :
            if char in counts :
                counts[char]+=1
            else:
                counts[char]=1
        sorted_keys=sorted(counts.keys(),key= lambda x: counts[x])

        result=[]
        for i in range (len(sorted_keys)-1,-1,-1):
            char =sorted_keys[i]
            result.append(char*counts[char])
        return "".join(result)


        
        
        