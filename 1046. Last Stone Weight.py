import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = list(stones)
        while len(heap)>=2:
            heapq.heapify(heap)
            largest_list = heapq.nlargest(2, heap)
            if largest_list[0] == largest_list[1]:
                heap.remove(largest_list[0])
                heap.remove(largest_list[0])
            else:
                heap.remove(largest_list[0])
                heap[heap.index(largest_list[1])] = abs(largest_list[0] - largest_list[1])
        return heap[0] if heap else 0
        
