class TimeMap:

    def __init__(self):
        self.mp = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mp:
            self.mp[key] = []
        self.mp[key].append((value, timestamp))

    def binary_search(self, arr, time):
        if time < arr[0][1] :
            return ""
        if time >= arr[-1][1]:
            return arr[-1][0]

        l, r = 0, len(arr) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if arr[mid][1] == time:
                return arr[mid][0]
            elif arr[mid][1] > time:
                r = mid - 1
            else:
                l = mid + 1

        return arr[r][0]

    def get(self, key: str, timestamp: int) -> str:
        arr = self.mp.get(key, [])
        if not arr:
            return "" 
        return self.binary_search(arr, timestamp)


# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
