class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for area in self.rows():
            if not self.isValidArea(area, board):
                return False
        for area in self.cols():
            if not self.isValidArea(area, board):
                return False
        for area in self.subBoxes():
            if not self.isValidArea(area, board):
                return False
        return True

    def row(self, i: int) -> List[int]:
        return [(i, j) for j in range(9)]

    def rows(self) -> List[List[int]]:
        return [self.row(i) for i in range(9)]

    def col(self, j: int) -> List[int]:
        return [(i, j) for i in range(9)]

    def cols(self) -> List[List[int]]:
        return [self.col(j) for j in range(9)]

    def subBox(self, top_left_i: int, top_left_j: int) -> List[int]:
        return [
            (top_left_i + i, top_left_j + j)
            for i in range(3)
            for j in range(3)
        ]

    def subBoxes(self) -> List[List[int]]:
        return [
            self.subBox(i, j)
            for i in range(0, 9, 3)
            for j in range(0, 9, 3)
        ]

    def isValidArea(self, area: List[int], board: List[List[str]]) -> bool:
        exists = {}
        for i in range(1, 10):
            exists[i] = False
        for i, j in area:
            if board[i][j] != ".":
                num = int(board[i][j])
                if exists[num]:
                    return False
                exists[num] = True
        return True
