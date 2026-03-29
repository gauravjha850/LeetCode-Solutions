class Solution(object):
    def rotate(self, arr, k):
        n=len(arr)
        k=k%n
        l=0
        r=n-1
        while l<r:
            arr[l],arr[r]=arr[r],arr[l]
            l=l+1
            r=r-1
        l=0
        r=k-1    
        while l<r:
            arr[l],arr[r]=arr[r],arr[l]
            l=l+1
            r=r-1
        l=k
        r=n-1

        while l<r:
            arr[l],arr[r]=arr[r],arr[l]
            l=l+1
            r=r-1
        return arr
        