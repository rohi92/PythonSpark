class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        ROW = len(board)
        COL = len(board[0])
        visited = set()

        def dfs(row, col, idx):
            if idx >= len(word):
                return True

            visited.add((row, col))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for direction in directions:
                new_row = row + direction[0]
                new_col = col + direction[1]
                #print(board[new_row][new_col],word[idx])
                if (new_row >= 0 and new_row < ROW and new_col >= 0 and new_col < COL and (new_row, new_col) not in visited
                        and board[new_row][new_col] == word[idx]):
                    if dfs(new_row, new_col, idx + 1):
                        return True
            visited.remove((row, col))
            return False

        for i in range(ROW):
            for j in range(COL):
                if board[i][j] == word[0]:
                    if dfs(i, j, 1):
                        return True
        return False

if __name__=="__main__":
    sol=Solution()
    print(sol.exist( board = [['C', 'A', 'P'], ['A', 'N', 'D'], ['T', 'I', 'E']], word = "CAT"))
