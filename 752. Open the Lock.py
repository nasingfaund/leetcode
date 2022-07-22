class Solution:
    def getNeighbors(self, node):
        neighbors = []
        dirs = [-1, 1]
        for i in range(len(node)):
            for direction in dirs:
                x = (int(node[i]) + direction) % 10
                neighbors.append(node[:i] + str(x) + node[i + 1:])
        return neighbors

    def openLock(self, deadends: List[str], target: str) -> int:
        start = "0000"
        if start in deadends:
            return -1
        
        if target == start:
            return 0
        
        deadends = set(deadends)
        queue = deque([[start, 0]])
        visited = set()
        while queue:
            num, depth = queue.popleft()
            visited.add(num)

            for neighbour in self.getNeighbors(num):
                    if neighbour == target:
                        return depth + 1
                    if neighbour not in deadends and neighbour not in visited:
                        queue.append((neighbour, depth + 1))
                        visited.add(neighbour)
        return -1
