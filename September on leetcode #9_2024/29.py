class AllOne:

    def __init__(self):
        self.mp = dict()

    def inc(self, key: str) -> None:
        if key not in self.mp:
            self.mp[key] = 0
        self.mp[key] += 1

    def dec(self, key: str) -> None:
        self.mp[key] -= 1
        if self.mp[key] == 0:
            del self.mp[key]

    def getMaxKey(self) -> str:
        if not self.mp:
            return ""
        mx = 0
        for key, val in self.mp.items():
            mx = max(mx, val)
        for key, val in self.mp.items():
            if val == mx:
                return key

    def getMinKey(self) -> str:
        if not self.mp:
            return ""
        mn = float('inf')
        for key,val in self.mp.items() :
            mn = min(mn,val)
        for key,val in self.mp.items() :
            if val == mn :
                return key

        # Your AllOne object will be instantiated and called as such:
        # obj = AllOne()
        # obj.inc(key)
        # obj.dec(key)
        # param_3 = obj.getMaxKey()
        # param_4 = obj.getMinKey()
# -------------------------------------------------------------------------------------------------


class AllOne:
    def __init__(self):
        self.myDict = {}

    def inc(self, key: str) -> None:
        if key in self.myDict:
            self.myDict[key] += 1
        else:
            self.myDict[key] = 1

    def dec(self, key: str) -> None:
        if key in self.myDict:
            if self.myDict[key] > 1:
                self.myDict[key] -= 1
            else:
                self.myDict.pop(key)

    def getMaxKey(self) -> str:
        if not self.myDict:
            return ""
        maxVal = max(self.myDict.values())
        for key in self.myDict.keys():
            if self.myDict[key] == maxVal:
                return key

    def getMinKey(self) -> str:
        if not self.myDict:
            return ""
        minVal = min(self.myDict.values())
        for key in self.myDict.keys():
            if self.myDict[key] == minVal:
                return key
