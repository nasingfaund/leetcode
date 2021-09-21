def longestNiceSubstring( s: str) -> str:
    ans = ""
    for i in range(len(s)):
        for j in range(i + 1, len(s)+1):
            if all(s[k].swapcase() in s[i:j] for k in range(i, j)):
                ans = max(ans, s[i:j], key=len)
    return ans
