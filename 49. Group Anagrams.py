class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
         return [list(group) for key, group in groupby(sorted(strs,key=sorted),sorted)]
        
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs.sort()
        sorted_strs = sorted(zip(strs, [''.join(i) for i in map(sorted, strs)]), key=lambda x: x[1])
        curr = None
        sub_res = []
        result = []
        for x, y in sorted_strs:
            if curr is None:
                curr = y
            if y == curr:
                sub_res.append(x)
            else:
                result.append(list(sub_res))
                sub_res = [x]
                curr = y
        if sub_res:
            result.append(list(sub_res))
        return result
