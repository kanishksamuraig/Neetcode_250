class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r=len(matrix);c=len(matrix[0])
        for i in range(r):
            low=0;high=c-1
            while(low<=high):
                mid=low+(high-low)//2
                if matrix[i][mid]==target:
                    return True
                elif matrix[i][mid]<target:
                    low=mid+1
                else:
                    high=mid-1
        return False
            