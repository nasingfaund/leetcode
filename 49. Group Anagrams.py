class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
         return [list(group) for key,group in groupby(sorted(strs,key=sorted),sorted)]
        
