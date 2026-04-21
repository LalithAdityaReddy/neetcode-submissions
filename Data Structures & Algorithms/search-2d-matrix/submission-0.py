class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m=len(matrix)
        n=len(matrix[0])    
        startRow=0
        endRow=m-1
        correctRow=-1
        while(startRow<=endRow):
            midRow=(startRow+endRow)//2
            if(matrix[midRow][0]<=target and matrix[midRow][n-1]>=target):
                correctRow=midRow
                break
            elif(matrix[midRow][n-1]<target):
                startRow=midRow+1
            elif(matrix[midRow][n-1]>target):
                endRow=midRow-1
        start=0
        end=n-1
        while(start<=end):
            mid=(start+end)//2
            if(matrix[correctRow][mid]==target):
                return True
            elif(matrix[correctRow][mid]<target):
                start=mid+1
            elif(matrix[correctRow][mid]>target):
                end=mid-1
        return False              
