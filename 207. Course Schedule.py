class Solution:
    def dfs(self, graph, node, white, gray, black):
        white.remove(node)
        gray.add(node)
        for neighbor in graph[node]:
            if neighbor in black:
                continue
            if neighbor in gray:
                return True

            if self.dfs(graph, neighbor, white, gray, black):
                return True
        gray.remove(node)
        black.add(node)
        return False


    def detect_cycle(self, graph, n):
        white = {*range(n)}
        gray = set()
        black = set()
        while white:
            curr = iter(white)
            if self.dfs(graph, next(curr), white, gray, black):
                return True
        return False
    
    def get_adjucency_list(self, edges):
        result = defaultdict(list)
        for dest, source in edges:
            result[source].append(dest)
        return result


    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        alist = self.get_adjucency_list(prerequisites)
        return not self.detect_cycle(alist, numCourses)
