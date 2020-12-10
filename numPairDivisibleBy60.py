
def numPairDivisibleBy60(time) -> int:
    rem = defaultdict(int)
    ret = 0
    for t in time:
        ret += rem[(60 - t % 60) % 60]
        rem[t % 60] += 1
    return ret

