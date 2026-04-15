class Solution(object):
    def next_smaller_element(self,heights):
        stack=[]
        n=len(heights)
        result=[n]*n
        
        for i in range (n-1,-1,-1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if not stack :
                result[i]=n
            else:
                result[i]=stack[-1]
            stack.append(i)
        return result
    
    def previous_smaller_element(self,heights):
        n=len(heights)

        stack=[]
        result=[-1]*n
        
        for i in range (n):
            while stack and heights[stack[-1]] >=heights[i]:
                stack.pop()
            if not stack :
                result[i]=-1
            else:
                result[i]=stack[-1]
            stack.append(i)
        return result
    
    def largestRectangleArea(self, heights):
        if not heights:
            return 0
        n=len(heights)
        pse=self.previous_smaller_element(heights)
        nse=self.next_smaller_element(heights)
        maxi=0
        for i in range (n):
            value=heights[i]*(nse[i]-pse[i]-1)
            maxi=max(maxi,value)
        return maxi

        