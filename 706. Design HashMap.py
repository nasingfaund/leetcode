class MyHashMap:
    def __init__(self):
        self.bucket = [[]] * 1000000

    def put(self, key: int, value: int) -> None:
        index = key % len(self.bucket)
        self.bucket[index] = [key, value]

    def get(self, key: int) -> int:
        index = key % len(self.bucket)
        try:
            return self.bucket[index][1]
        except:
            return -1

    def remove(self, key: int) -> None:
        index = key % len(self.bucket)
        self.bucket[index] = []
