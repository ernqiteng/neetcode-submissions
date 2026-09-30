class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def row(rownum):
            nums = []
            for num in board[rownum]:
                if num != ".":
                    nums.append(num)
            if len(set(nums)) != len(nums):
                print("row")
                return False
            return True
        
        def column(colnum):
            nums = []
            for i in range(len(board)):
                if board[i][colnum] != ".":
                    nums.append(board[i][colnum])
            if len(set(nums)) != len(nums):
                print("col")
                return False
            return True

        def box(x,y):
            nums = []
            for i in range(x, x+3):
                for j in range(y, y+3):
                    if board[i][j] != ".":
                        nums.append(board[i][j])
            if len(set(nums)) != len(nums):
                print("box")
                return False
            return True

        #check each row for duplicates
        for i in range(len(board)):
            if not row(i):
                return False
        
        #check each column
        for i in range(len(board[0])):
            if not column(i):
                return False

        #check each subbox
        boxcorners = [[0,0], [0,3], [0,6],
            [3,0], [6,0],
            [3,3], [3,6],
            [6,3], [6,6]]
        
        for x,y in boxcorners:
            if not box(x,y):
                return False

        #if any of them are false return false

        return True


       

