class TimeMap:
    def __init__(self):
        self.d={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        currentlist=self.d.get(key,[])
        currentlist.append([timestamp,value])
        self.d[key]=currentlist

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""
        low=0;high=len(self.d[key])-1
        while low<=high:
            mid=low+(high-low)//2
            if self.d[key][mid][0]==timestamp:
                return self.d[key][mid][1]
            elif self.d[key][mid][0]<timestamp:
                low=mid+1
            else:
                high=mid-1
        return self.d[key][high][1] if timestamp>=self.d[key][high][0] else ""
