class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp={}
        def helper(amount,i,curr_sum):
            if i>=len(coins):
                return 1 if curr_sum==amount else 0
            if(i,curr_sum) in dp:
                return dp[(i,curr_sum)]
            include=0
            if(curr_sum+coins[i]<=amount):
                include=helper(amount,i,curr_sum+coins[i])
            exclude=helper(amount,i+1,curr_sum)
            dp[(i,curr_sum)]=include+exclude
            return dp[(i,curr_sum)]
        return helper(amount,0,0)