class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap=[]
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        for key,val in d.items():
            heapq.heappush(heap,(val,key))
            if len(heap)>k:
                heapq.heappop(heap)
        return [item for val,item in heap]
