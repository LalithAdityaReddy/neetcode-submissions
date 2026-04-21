import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans=[]
        heap=[]
        x1,y1=0,0
        for point in points:
            x2=point[0]
            y2=point[1]
            val=math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
            heapq.heappush(heap,(val,x2,y2))
        heapq.heapify(heap)
        while k>0:
            dist,x,y=heapq.heappop(heap)
            ans.append([x,y])
            k-=1
        return ans