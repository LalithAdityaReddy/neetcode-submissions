class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lp=0
        rp=len(heights)-1
        area=0
        while(lp<rp):
            height=min(heights[lp],heights[rp])
            width=rp-lp
            area=max(area,height*width)
            if heights[lp]<heights[rp]:
                lp+=1
            else:
                rp-=1
        return area