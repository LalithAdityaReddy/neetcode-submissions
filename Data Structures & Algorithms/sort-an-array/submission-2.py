class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heap=[]
        for i in nums:
            heapq.heappush(heap,i)
        return [heapq.heappop(heap) for _ in range(len(nums))]