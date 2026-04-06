class Solution(object):
    def robotSim(self, commands, obstacles):
        dx=[0,1,0,-1]
        dy=[1,0,-1,0]
        x,y=0,0
        direction=0
        obs_set={(x,y)for x,y in obstacles}
        max_dist=0
        for cmd in commands:
            if cmd==-2:
                direction=(direction-1)%4
            elif cmd==-1:
                direction=(direction+1)%4
            else:
                for steps in range (cmd):
                    next_x= x+dx[direction]
                    next_y= y+dy[direction]

                    if (next_x,next_y) in obs_set :
                        break
                    x,y=next_x,next_y
            max_dist=max(max_dist,x**2+y**2)
        return max_dist

        