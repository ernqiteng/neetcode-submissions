class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #checking if each row contains duplicates
        items = 0
        row = set()
        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                if board[i][j] != ".":
                    row.add(board[i][j])
                    items += 1
            if items != len(row):
                return False
            else:
                row = set()
                items = 0
        
        #checking if each column contains duplicates
        items = 0
        column = set()
        for i in range(0, 9):
            for j in range(0, 9):
                if board[j][i] != ".":
                    column.add(board[j][i])
                    items += 1
            if items != len(column):
                return False
            else:
                column = set()
                items = 0

        #checking if each sub-box contains duplicates
        items = 0
        subbox = set()
        for k in range(0, 3):
            for l in range(0, 3):
                for i in range(3*k, 3*k+3):
                    for j in range(3*l, 3*l+3):
                        if board[i][j] != ".":
                            subbox.add(board[i][j])
                            items += 1
                if items != len(subbox):
                    return False
                else:
                    subbox = set()
                    items = 0

        return True