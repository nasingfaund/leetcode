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

                
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        seen = set()

        def dfs(i):
            for j in range(n):
                if isConnected[i][j] == 1 and j not in seen:
                    seen.add(j)
                    dfs(j)

        count = 0
        for i in range(n):
            if i not in seen: 
                dfs(i)
                count += 1

        return count
