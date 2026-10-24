class Solution:
    def coordinates(self, i: int, m: int, n: int) -> tuple[int, int]:
        col = i % n
        row = (i - col) // n
        return row, col

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        start = 0
        start_row, start_col = self.coordinates(start, m, n)
        end = m * n - 1
        end_row, end_col = self.coordinates(end, m, n)
        length = end - start + 1
        while start <= end:
            if matrix[start_row][start_col] == target:
                return True
            if matrix[end_row][end_col] == target:
                return True

            if start == end:
                mid = start
            else:
                mid = start + length // 2

            mid_row, mid_col = self.coordinates(mid, m, n)
            if matrix[mid_row][mid_col] == target:
                return True
            elif matrix[mid_row][mid_col] < target:
                start = mid + 1
                start_row, start_col = self.coordinates(start, m, n)
            else:
                end = mid - 1
                end_row, end_col = self.coordinates(end, m, n)

            length = end - start + 1
        return False
