def num_islands(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    queue = []
    count = 0

    def is_valid(row, col):
        return not (row < 0 or row == num_rows or col < 0 or col == num_cols)
            
    def bfs():
        queue.append( (row, col) )
        matrix[row][col] = 0
        
        while queue:
            row, col = queue.pop(0)
            dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            for d in dirs:
                new_row, new_col = row + d[0], col + d[1] 
                if is_valid(new_row, new_col) and matrix[new_row][new_col] == 1:
                    queue.append( (new_row, new_col) )
                    matrix[new_row][new_col] = 0 #mark visited 

    for row in range(num_rows):
        for col in range(num_cols):
            if (matrix[row][col] == 1):
                bfs()
                count += 1
    return count

      
test = [
    [1, 1, 1],
    [0, 0, 0],
    [1, 1, 1],
    [1, 1, 1]
]

print(num_islands(test))