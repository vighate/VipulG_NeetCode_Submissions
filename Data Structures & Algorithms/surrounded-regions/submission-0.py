class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return []
        rows = len(board)
        cols = len(board[0])

        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols or board[r][c] != "O":
                return 
            board[r][c] = "T"
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r,c-1)
        
        for row in range(rows):
            dfs(row,0)
            dfs(row,cols-1)
        for col in range(cols):
            dfs(0,col)
            dfs(rows-1,col)
        for i in range(rows):
            for j in range(cols):
                if board[i][j] =="O":
                    board[i][j] ="X"
                elif board[i][j] =="T":
                    board[i][j] ="O"
        