class Solution(object):
    def trap(self, arr):
        n=len(arr)
        if n<3:
            return 0
        left_max=[0]*n
        right_max=[0]*n
        total=0
        left_max[0]=arr[0]
        for i in range(1,n):
            
            left_max[i]=max(left_max[i-1],arr[i])
        right_max[n-1]=arr[n-1]
        for i in range (n-2,-1,-1):
            right_max[i]=max(right_max[i+1],arr[i])
        for i in range (n):
            if arr[i] < right_max and arr[i] < left_max :
                k= min(right_max[i],left_max[i])-arr[i]
                total=total + k
        return total




        