class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        direc=[[-1,0],[1,0],[0,1],[0,-1]]
        def func(i,j):
            ans=1
            l=0
            for dr,dc in direc:
                nr=dr+i
                nc=dc+j
                if(0<=nr<len(matrix) and 0<=nc<len(matrix[0]) and matrix[nr][nc]>matrix[i][j]):
                    l=1+func(nr,nc)
                    ans=max(ans,l)
            return ans
        f=0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                f=max(f,func(i,j))
        return f

