def count_components(graph):
    visited = set()
    count = 0

    def dfs(graph, start, visited):
        visited.add(start)
        for node in graph[start]:
            if node not in visited:
                dfs(graph, node, visited)

    for node in graph:
        if node not in visited:
            count += 1
            dfs(graph, node, visited)
    return count


assert count_components(get_adjacency_list([[0, 1], [1, 2], [3, 4]])) == 2
assert count_components(get_adjacency_list([[0, 1], [1, 2], [2, 3], [3, 4]])) == 1
