# TLE
class Solution:
    def get_adjucency_list(self, edges, n):
        adict = {key: [] for key in range(n)}
        for s, d in edges:
            adict[s].append(d)
            adict[d].append(s)
        return adict
    
    def find_height(self, alist, start):
        

        def _find_height(alist, start, visited):
            visited.add(start)
            ans = 0
            for node in alist[start]:
                if node not in visited:
                    ans = max(ans, _find_height(alist, node, visited) + 1)
            return ans

        return _find_height(alist, start, set())


    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        alist = self.get_adjucency_list(edges, n)
        result = defaultdict(lambda: 0)
        for node in range(n):
            result[node] = self.find_height(alist, node)
        min_height = min(result.values())
        return [k for k, v in result.items() if v == min_height]
