class Solution(object):
    def bestTower(self, towers, center, radius):
        cx,cy=center
        best_tower=[-1,-1]
        best_quality=-1
        for x,y,q in towers:
            distance=abs(cx-x)+abs(cy-y)
            if distance <=radius:
                if q > best_quality:
                    best_quality=q
                    best_tower=[x,y]
                elif q==best_quality:
                    
                    if x < best_tower[0] or (x==best_tower[0] and y< best_tower[1]):
                        best_tower=[x,y]
        return best_tower
        
        