class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        most_common = Counter(nums).most_common(k)
        return [k for k, count in most_common]
      
# bucket sort
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        ranked = [[] for _ in range(len(nums) + 1)]
        c = Counter(nums)
        for key, val in c.items():
            ranked[val].append(key)
        return list(chain(*ranked))[-k:]
