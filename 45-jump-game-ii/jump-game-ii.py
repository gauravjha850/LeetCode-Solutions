class Solution(object):
    def jump(self, nums):
        jumps=0
        current_jump_end=0
        furthest_we_can_jump=0
        for i in range (len(nums)-1):
            furthest_we_can_jump=max(i+nums[i],furthest_we_can_jump)
            if i == current_jump_end:
                jumps=jumps+1

                current_jump_end=furthest_we_can_jump
        return jumps


        