# very similar to Longest Substring with maximum K Distinct Characters (educative)
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start = 0
        max_len = 0
        adict = {}

        for end in range(len(fruits)):
            if fruits[end] not in adict:
                adict[fruits[end]] = 0
            adict[fruits[end]] += 1

            while len(adict) > 2: # only this line is diffrent, 2 instead of k

                adict[fruits[start]] -= 1
                if adict[fruits[start]] == 0:
                    adict.pop(fruits[start])
                start += 1
            max_len = max(max_len, end - start + 1)
        return max_len

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_len = 0
        adict = defaultdict(int)

        left = right = 0

        while right < len(fruits):
            adict[fruits[right]] += 1

            while len(adict) > 2:
                max_len = max(max_len, right - left)
                adict[fruits[left]] -= 1
                if adict[fruits[left]] == 0:
                    adict.pop(fruits[left])
                left += 1

            right += 1

        return max(max_len, right - left)
