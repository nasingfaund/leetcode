# bfs 
def validTree(n, edges):
    visited = set()
    queue = deque([(0, -1)])
    graph = get_adjacency_list(edges=edges)
    while queue:
        root, parent = queue.popleft()
        visited.add(root)
        for node in graph[root]:
            if node == parent:
                continue
            if node in visited:
                return False
            queue.append((node, root))

    return len(visited) == n

# dfs iterative
def validTree(n, edges):
    visited = set()
    stack = [(0, -1)]
    graph = get_adjacency_list(edges=edges)
    while stack:
        root, parent = stack.pop()
        visited.add(root)
        for node in graph[root]:
            if node == parent:
                continue
            if node in visited:
                return False
            stack.append((node, root))

    return len(visited) == n


def validTree(n, edges):
    def dfs(graph, start, visited):
        visited.add(start)
        for node in graph[start]:
            if node not in visited:
                dfs(graph, node, visited)
        return visited

    def get_adjacency_list(edges):
        result = defaultdict(list)
        for dest, source in edges:
            result[source].append(dest)
            result[dest].append(source)
        return result

    visited = set()
    graph = get_adjacency_list(edges=edges)
    dfs(graph, 0, visited)
    return len(visited) == n and len(edges) == n - 1


def is_cycle(graph, start, parent, visited):
    visited.add(start)
    for node in graph[start]:
        if node == parent:
            continue
        if node in visited:
            return True
        if is_cycle(graph, node, start, visited):
            return True
    return False


def valid_tree(n, edges):
    def get_adjacency_list(edges):
        result = defaultdict(list)
        for dest, source in edges:
            result[source].append(dest)
            result[dest].append(source)
        return result

    visited = set()
    graph = get_adjacency_list(edges=edges)
return not is_cycle(graph, 0, -1, visited) and len(visited) == n

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
