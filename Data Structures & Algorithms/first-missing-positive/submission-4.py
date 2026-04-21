class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)
        d={}
        for i in range(1,n+1):
            d[i]=d.get(i,0)+1
        for i in d.keys():
            if i not in nums and i>0:
                return i
        return list(d)[-1]+1
        

