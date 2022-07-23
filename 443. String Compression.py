class Solution:
    def compress(self, chars: List[str]) -> int:
        result = []
        for k, group in groupby(chars):
            result.append(k)
            count = len(list(group))
            if count > 1:
                result.extend(list(str(count)))
        chars[:] = result[:]
        return len(result)        
