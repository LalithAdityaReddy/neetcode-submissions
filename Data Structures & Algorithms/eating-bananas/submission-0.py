import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=sum(piles)
        def isvalid(k):
            cnt=0
            for pile in piles:
                cnt+=math.ceil(pile/k)
            return cnt
        while l<=r:
            mid=(l+r)//2
            val=isvalid(mid)
            if val<=h:
                r=mid-1
            else:
                l=mid+1
        return l