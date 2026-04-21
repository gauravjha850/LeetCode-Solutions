class Solution(object):
    def lemonadeChange(self, arr):
        n=len(arr)
        five=0
        ten=0
        for i in range (n):
            if arr[i] == 5 :
                five=five+1
            elif arr[i] == 10:
                if five:
                    five=five-1
                    ten=ten+1
                else:
                    return False
            else:
                if five and ten :
                    five=five-1
                    ten=ten-1
                elif five >=3 :
                    five=five-3
                else:
                    return False
        return True


        