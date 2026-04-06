class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefmatrix=[]
        for row in matrix:
            l=[];n=0
            for col in row:
                n+=col
                l.append(n)
            self.prefmatrix.append(l)
        print(self.prefmatrix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum=0
        if col1==0:
            for i in range(row1,row2+1):
                sum+=self.prefmatrix[i][col2]
        else:
            for i in range(row1,row2+1):
                sum+=self.prefmatrix[i][col2]-self.prefmatrix[i][col1-1]
        return sum



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)