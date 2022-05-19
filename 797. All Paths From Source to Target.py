# time complexity: O(N*N^2) 
# 1) There are ~ O(2^N) paths;
# 2) Each path has a length ~ O(N);
# 3) Appending each path to result should be ~ O(N2^N).

The time & space complexity should be O(N2^N).
class Solution(object):
    def dfs(self, graph, path, result):
        if path[-1] == len(graph) - 1:
            result.append(path)
        else:
            for child in graph[path[-1]]:
                self.dfs(graph, path + [child], result)
            
    def allPathsSourceTarget(self, graph):
        result = []
        self.dfs(graph, [0], result)
        return result

# dfs
class Solution(object):
    def allPathsSourceTarget(self, graph):
        stack = [[0]]
        result = []
        while stack:
            path = stack.pop()
            if path[-1] == len(graph) - 1:
                result.append(path)
                
            for child in graph[path[-1]]:
                stack.append(path+[child])
                
        return result
      
      
# bfs 
class Solution(object):
    def allPathsSourceTarget(self, graph):
        queue = deque([[0]])
        result = []

        while queue:
            path = queue.popleft()

            if path[-1] == len(graph) - 1:
                result.append(path)
            else:
                for n in graph[path[-1]]:
                    queue.append(path + [n])

        return result
