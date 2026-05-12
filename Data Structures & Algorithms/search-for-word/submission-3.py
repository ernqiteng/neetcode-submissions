class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [[0, 1], [-1, 0], [0, -1], [1, 0]]

        def backtrack(row, col, path, currword):
            if currword == word:
                return True
            
            for r, c in directions:
                if 0 <= (row+r) < len(board) and 0<=(col+c)<len(board[0]):
                    if [row+r, col+c] not in path:
                        if board[row+r][col+c] == word[len(currword)]:
                            path.append([row+r,col+c])
                            if backtrack(row+r,col+c,path, currword + board[row+r][col+c]):
                                return True
                            path.pop()
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if backtrack(i,j, [[i,j]], board[i][j]):
                        return True
        return False