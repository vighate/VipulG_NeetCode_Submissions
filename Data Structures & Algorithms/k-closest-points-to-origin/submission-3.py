import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        res = []
        for point in points:
            x,y = point
            dist = ((x-0)**2 + (y-0)**2)
            res.append([dist,x,y])
        
        res = sorted(res, key = lambda x:x[0])
        stack = []
        for dist,x,y in res[:k]:
            stack.append([x,y])
                
        return stack