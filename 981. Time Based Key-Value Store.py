class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        alist = self.time_map[key] 
        
        first = 0
        second = len(alist)
        
        while first < second:
            middle = (first + second) // 2
            key, timestamp_prev = alist[middle]
            if timestamp_prev <= timestamp:
                first = middle + 1
            elif timestamp_prev > timestamp:
                second = middle
        return "" if second == 0 else alist[second-1][0]
