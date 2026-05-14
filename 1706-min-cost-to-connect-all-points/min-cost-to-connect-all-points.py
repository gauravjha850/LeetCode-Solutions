import heapq
class Solution(object):
    def minCostConnectPoints(self, point):
        n=len(point)
        visited=[False]*n
        min_heap=[(0,0)]    # ist is the cost and secoond is the node in which it will go 
        used_nodes=0
        total_cost=0
        while used_nodes<n:
            cost,nodes=heapq.heappop(min_heap)
            if visited[nodes]:

                continue
            visited[nodes]=True
            used_nodes+=1
            total_cost+=cost
            x1,y1=point[nodes]
            for j in range (n):
                if not visited[j]:
                    x2,y2=point[j]
                    dist=abs(x2-x1)+abs(y2-y1)
                    heapq.heappush(min_heap,(dist,j))
        return total_cost
