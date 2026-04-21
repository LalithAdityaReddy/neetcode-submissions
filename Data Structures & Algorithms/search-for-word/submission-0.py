class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m=len(board)
        n=len(board[0])
        def helper(board,i,j,idx):
            if(idx==len(word)):
                return True
            if i<0 or i>=m or j<0 or j>=n or visited[i][j] or board[i][j]!=word[idx]:
                return False
            visited[i][j]=True
            bottom=helper(board,i+1,j,idx+1)
            left=helper(board,i-1,j,idx+1)
            right=helper(board,i,j+1,idx+1)
            up=helper(board,i,j-1,idx+1)
            visited[i][j]=False
            return right or left or bottom or up
        visited=[[False]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if helper(board,i,j,0):
                        return True
        return False



        