class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums=[]
        for i in range(1,n+1):
            nums.append(i)
        self.ans=[]
        def helper(idx,comb):
            if len(comb)==k:
                self.ans.append(comb.copy())
                return
            if idx>=len(nums):
                return
            if len(comb)>k:
                return
            comb.append(nums[idx])
            helper(idx+1,comb)
            comb.pop()
            helper(idx+1,comb)
            return 
        helper(0,[])
        return self.ans
        
            