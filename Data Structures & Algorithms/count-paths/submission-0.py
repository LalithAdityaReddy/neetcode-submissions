class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        directions=[[1,0],[0,1]]
        d={}
        def dfs(i,j):
            if((i,j) in d):
                return d[(i,j)]
            if i==m-1 and j==n-1:
                return 1
            ans=0
            for dr,dc in directions:
                nr=i+dr
                nc=j+dc
                if(0<=nr<m and 0<=nc<n):
                    ans+=dfs(nr,nc)
            d[(i,j)]=ans
            return d[(i,j)]
        return dfs(0,0)
            

