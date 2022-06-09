# Tree is a connected acyclic undirected graph.
# or we can use condition len(visited) == n and len(edges) == n-1
def dfs(graph, root, parent, visited):
    visited.add(root)
    for node in graph[root]:
        if node == parent:
            continue
        if node in visited: # continue
            return False

        if not dfs(graph, node, root, visited): #dfs(node)
            return False
    return True


def validTree(n, edges):
    graph = defaultdict(list)
    for src, dest in edges:
        graph[src].append(dest)
        graph[dest].append(src)
    visited = set()

    return dfs(graph, 0, -1, visited) and len(visited) == n


assert validTree(5, [[0,1], [1,2], [2,3], [1,3], [1,4]]) == False
assert validTree(5, [[0,1], [0,2], [0,3], [1,4]]) == True
