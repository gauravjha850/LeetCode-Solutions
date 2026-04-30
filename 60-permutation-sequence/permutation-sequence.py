import math
class Solution(object):
    def getPermutation(self, n, k):
        numbers=[i for i in range (1,n+1)]

        k=k-1
        result=[]
        for i in range (n-1,-1,-1):
            fact=math.factorial(i)

            index=k//fact

            chosen_number=numbers[index]

            result.append(str(chosen_number))

            numbers.pop(index)

            k=k%fact

        return "".join(result)
