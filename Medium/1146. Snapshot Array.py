class SnapshotArray:

    def __init__(self, length: int):
        self.arr = [[] for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        if not self.arr[index] or self.arr[index][-1][1] != self.snap_id:
            self.arr[index].append((val, self.snap_id))
        else:
            self.arr[index][-1] = (val, self.snap_id)

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def search(self, lst, snapshot) -> int:
        l, r = 0, len(lst) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if lst[mid][1] == snapshot:
                return lst[mid][0]
            elif lst[mid][1] < snapshot:
                l = mid + 1
            else:
                r = mid - 1

        return lst[r][0] if r >= 0 else 0

    def get(self, index: int, snap_id: int) -> int:
        lst = self.arr[index]
        if not lst:
            return 0
        return self.search(lst, snap_id)

        
        
        # Your SnapshotArray object will be instantiated and called as such:
        # obj = SnapshotArray(length)
        # obj.set(index,val)
        # param_2 = obj.snap()
        # param_3 = obj.get(index,snap_id)
