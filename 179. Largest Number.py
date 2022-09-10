class Solution:
    def largestNumber(self, nums):
        def key(x, y):
            if x + y < y + x:
                return 1
            elif x == y:
                return 0
            else:
                return -1
        largest_num = ''.join(sorted(map(str, nums), key=cmp_to_key(key)))
        return '0' if largest_num[0] == '0' else largest_num
