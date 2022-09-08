def find_longest_substring(string, k):
    curr = defaultdict(int)
    left = right = 0
    max_length = 0

    while right < len(string):
        curr[string[right]] += 1

        while len(curr) > k:
            curr[string[left]] -= 1
            if curr[string[left]] == 0:
                curr.pop(string[left])
            left += 1

        max_length = max(max_length, right - left + 1)

        right += 1

    return max_length


assert find_longest_substring("araaci", 2) == 4
assert find_longest_substring("araaci", 1) == 2
assert find_longest_substring("cbbebi", 3) == 5
assert find_longest_substring("cbbebi", 10) == 6
