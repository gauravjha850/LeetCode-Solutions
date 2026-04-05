class Solution(object):
    def mirrorFrequency(self, s):
        def get_mirror(char):
            if char.isdigit():
                return str(9-int(char))
            else:
                code=ord(char)
                position=code-96
                mirror_position=27-position
                return chr(mirror_position+96)
        mp=defaultdict(int)
        for i in s:
            mp[i]=mp[i]+1
        count=0
        for key,value in mp.items():
            mirror=get_mirror(key)
            if mirror not in mp:
                count=count+value
            elif mp[mirror] > value:
                count=count+(mp[mirror]-value)
        return count
                
        
        