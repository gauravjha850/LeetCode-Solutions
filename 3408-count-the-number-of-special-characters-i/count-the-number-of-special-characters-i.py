class Solution(object):
    def numberOfSpecialChars(self, word):
        char_set=set(word)
        count=0
        for char in char_set:
            if char.islower() and char.upper() in char_set:
                count+=1
        return count 
            

            

        