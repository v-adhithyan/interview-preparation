class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        paths = []
        left = 0, -1
        right = 0, 1
        up = -1, 0
        down = 1, 0
        visited = set()
        m = len(matrix)
        n = len(matrix[0])
        next_direction = {
            right: down,
            down: left,
            left: up,
            up: right
        }

        if m == 1:
            return matrix[0]
        if n == 1:
            for i in range(m):
                paths.append(matrix[i][0])
            return paths

        def is_out_of_bounds(i, j):
            return i < 0 or i >= m or j < 0 or j >= n
        
        def spiral(mat, i, j, direction):
            if i < 0:
                spiral(mat, 0, j, direction)
            elif j < 0:
                spiral(mat, i, 0, direction)
            elif i >= m:
                spiral(mat, m-1, j, direction)
            elif j >= n:
                spiral(mat, i, n-1, direction)
            elif (i, j) in visited:
                current_direction = direction
                while (i, j) in visited:
                    direction = next_direction[direction]
                    if direction == current_direction:
                        return
                    i += direction[0]
                    j += direction[-1]
                spiral(mat, i, j, direction)
            else:
                while True:
                    if is_out_of_bounds(i, j):
                        break
                    if (i, j) in visited:
                        i -= direction[0]
                        j -= direction[-1]
                        break
                    paths.append(mat[i][j])
                    visited.add((i, j))
                    i += direction[0]
                    j += direction[-1]
                spiral(mat, i, j, direction)
        
        spiral(matrix, 0, 0, right)
        return paths
    

# Best solution from leetcode
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        xmin = -1
        xmax = len(matrix)
        ymin = -1
        ymax = len(matrix[0])
        x = y = 0
        res = [matrix[0][0]]

        while xmin <= xmax and ymin <= ymax:
            for i, direction in enumerate([[0,1],[1,0],[0,-1],[-1,0]]):
                while xmin < x + direction[0] < xmax and ymin < y + direction[1] < ymax:
                    x += direction[0]
                    y += direction[1]
                    res.append(matrix[x][y])
                if i == 0:
                    xmin += 1
                elif i == 1:
                    ymax -= 1
                elif i == 2:
                    xmax -= 1
                elif i == 3:
                    ymin += 1
                if xmin + 1 == xmax or ymin + 1 == ymax:
                    break
        return res