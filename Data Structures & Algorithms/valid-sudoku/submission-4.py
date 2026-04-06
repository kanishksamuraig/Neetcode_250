class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        set3=set()
        for i in range(9):
            set1=set()
            set2=set()
            for j in range(9):
                if board[i][j]!=".":
                    if board[i][j] in set1:
                        return False
                    else:
                        set1.add(board[i][j])
                    s=f"The element {board[i][j]} is in box {i//3} {j//3}"
                    print(s)
                    if s in set3:
                        return False
                    else:
                        set3.add(s)
                if board[j][i]!=".":
                    if board[j][i] in set2:
                        return False
                    else:
                        set2.add(board[j][i])
        return True
