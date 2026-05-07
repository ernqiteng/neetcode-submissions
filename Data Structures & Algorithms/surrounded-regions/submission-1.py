class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = [[0,-1], [0, 1], [1, 0], [-1, 0]]
        edge_os = []

        #checking edge characters for "O"
        for col in range(len(board[0])):
            if board[0][col] == "O":
                edge_os.append([0,col])
                board[0][col] = "T"
        
        for col in range(len(board[-1])):
            if board[-1][col] == "O":
                edge_os.append([len(board)-1,col])
                board[-1][col] = "T"
        
        for row in range(len(board)):
            if board[row][0] == "O":
                edge_os.append([row,0])
                board[row][0] = "T"
        
        for row in range(len(board)):
            if board[row][-1] == "O":
                edge_os.append([row,len(board[row])-1])
                board[row][-1] = "T"
        
        #dfs on edge "O"s, marks with "T"
        while edge_os:
            curr_row, curr_col = edge_os.pop()
            for r, c in directions:
                if 0 <= (curr_row+r) < len(board) and 0<= (curr_col+c) < len(board[0]):
                    if board[curr_row+r][curr_col+c] == "O":
                        edge_os.append([curr_row+r,curr_col+c])
                        board[curr_row+r][curr_col+c] = "T"

        #all remaining "O"s can be converted to "X"s, change "T"s back to "O"s
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "T":
                    board[row][col] = "O"