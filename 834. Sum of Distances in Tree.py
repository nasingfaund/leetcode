# TLE, reuse previously computed distances
class Solution:
    def get_adjacency_list(self, edges):
        graph = defaultdict(list)
        for src, dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)
        return graph
            
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = self.get_adjacency_list(edges)
        def dfs(start, depth, visited):
            visited.add(start)
            ans = 0
            for node in graph[start]:
                if node not in visited:
                    ans += dfs(node, depth + 1, visited) 
            ans += depth
            return ans
        
        
        result = []
        for i in range(n):
            result.append(dfs(i, 0, set()))
        return result
