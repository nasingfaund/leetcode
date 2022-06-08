def get_shortest_path(grid):
    n = len(grid)
    m = len(grid[0])
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    queue = deque()

    for i in range(n):
        for j in range(m):
            if grid[i][j] == '*':
                queue.append((i, j))
                grid[i][j] = 0
                break

    while queue:
        i, j = queue.popleft()

        for x, y in directions:
            new_i = i + x
            new_j = j + y

            if 0 <= new_i < n and 0 <= new_j < m:
                if grid[new_i][new_j] == '#':
                    return grid[i][j] + 1
                if grid[new_i][new_j] != 'X' and grid[new_i][new_j] != 0:
                    grid[new_i][new_j] = grid[i][j] + 1
                    queue.append((new_i, new_j))
    return -1


assert get_shortest_path([
    ["X", "X", "X", "X", "X", "X"],
    ["X", "*", "O", "O", "O", "X"],
    ["X", "O", "O", "#", "O", "X"],
    ["X", "X", "X", "X", "X", "X"]]) == 3

assert get_shortest_path([
    ["X", "X", "X", "X", "X"],
    ["X", "*", "X", "O", "X"],
    ["X", "O", "X", "#", "X"],
    ["X", "X", "X", "X", "X"]]) == -1

assert get_shortest_path([
    ["X", "X", "X", "X", "X", "X", "X", "X"],
    ["X", "*", "O", "X", "O", "#", "O", "X"],
    ["X", "O", "O", "X", "O", "O", "X", "X"],
    ["X", "O", "O", "O", "O", "#", "O", "X"],
    ["X", "X", "X", "X", "X", "X", "X", "X"]]) == 6

assert get_shortest_path([["O", "*"], ["#", "O"]]) == 2

assert get_shortest_path([["X", "*"], ["#", "X"]]) == -1
