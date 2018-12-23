#largest island

def find_largest_island(matrix):
    visited = set()
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    max_size = 0

    def helper(row, col):
        if (row, col) in visited or row == num_rows or col == num_cols or row < 0 or col < 0 or matrix[row][col] == 0:
            return 0
        else:
            visited.add( (row, col) )
            return 1 + helper(row, col + 1) + helper(row + 1, col) + helper(row - 1, col) + helper(row, col - 1) 
    
    for row in range(num_rows):
        for col in range(num_cols):
            size = helper(row, col)
            max_size = max(size, max_size)
    return max_size

      
test = [
    [1, 1, 1],
    [0, 0, 0],
    [1, 1, 1],
    [1, 1, 1]
]

print(find_largest_island(test))