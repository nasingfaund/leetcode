def is_path_exists(maze, start: Tuple[int, int], dest: Tuple[int, int]) -> bool:
    n = len(maze)
    m = len(maze[0])

    visited = set()
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    x0, y0 = start
    x1, y1 = dest

    def dfs(i, j):
        if i < 0 or i >= n or j < 0 or j >= m:
            return False
        if i == x1 and j == y1:
            return True

        visited.add((i, j))
        for x, y in directions:
            new_i = i + x
            new_j = j + y
            while 0 <= new_i + x < n and 0 <= new_j + y < m and maze[new_i][new_j] == 0:
                new_i += x
                new_j += y
            if (new_i, new_j) not in visited and dfs(new_i, new_j):
                return True
        return False

    return dfs(x0, y0)
  
assert is_path_exists([
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0]
], (0, 4), (4, 4)) == True

assert is_path_exists([
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0]
], (0, 4), (3, 2)) == False

