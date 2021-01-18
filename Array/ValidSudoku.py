class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            #check row
            if board[i].count('.') + len(set(board[i])) < 10:
                return False
            
            #check column
            arr = [board[j][i] for j in range (9)]
            if arr.count('.') + len(set(arr)) < 10:
                return False
            
            #check 3x3
            arr = [board[3*(i//3)+j][3*(i%3)+k] for j in range(3) for k in range(3)]
            if arr.count('.') + len(set(arr)) < 10:
                return False
            # arr1 = []
            # arr2 = []
            # for j in range(9):
            #     arr1.append(board[j][i])
            #     arr2.append(board[3*(i//3) + (j//3)][3*(i%3) + (j%3)])
            # if arr1.count('.') + len(set(arr1)) < 10:
            #     return False
            # if arr2.count('.') + len(set(arr2)) < 10:
            #     return False

        # for i in range(9):
        #     arr0=[]
        #     arr1=[]
        #     arr2=[]
        #     for j in range(9):
        #         if board[i][j] != '.':
        #             arr0.append(board[i][j])
        #         if board[j][i] !='.':
        #             arr1.append(board[j][i])
        #         ind1 = 3*(i//3) + (j//3)
        #         ind2 = 3*(i%3) + (j%3)
        #         if board[ind1][ind2] != '.':
        #             arr2.append(board[ind1][ind2])
        #     if len(arr0) != len(set(arr0)):
        #         return False
        #     elif len(arr1) != len(set(arr1)):
        #         return False
        #     elif len(arr2) != len(set(arr2)):
        #         return False
            
        return True
