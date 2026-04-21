class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2:
            return False
        target=sum(nums)//2
        n=len(nums)
        dp=set()
        dp.add(0)
        for i in nums[::-1]:
            new_dp=dp.copy()
            for val in dp:
                new_dp.add(i+val)
            dp=new_dp
        return True if target in dp else False


            