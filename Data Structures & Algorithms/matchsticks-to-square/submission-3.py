class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks)%4!=0:
            return False
        maxi=sum(matchsticks)//4
        matchsticks.sort(reverse=True)
        sides=[0]*4
        def func(i):
            if i==len(matchsticks):
                return True
            for j in range(4):
                if sides[j]+matchsticks[i]<=maxi:
                    sides[j]+=matchsticks[i]
                    if func(i+1):
                        return True
                    sides[j]-=matchsticks[i]
            return False
        return func(0)
                
                
        
            
        
            