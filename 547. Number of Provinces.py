class Solution:
    def get_graph(self, alist):
        n = len(alist)
        adict = defaultdict(set)
        for i in range(n):
            for j in range(n):
                if alist[i][j] == 1:
                    adict[i].add(j)
                    adict[j].add(i)
        return dict(adict)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = self.get_graph(isConnected)
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

                
