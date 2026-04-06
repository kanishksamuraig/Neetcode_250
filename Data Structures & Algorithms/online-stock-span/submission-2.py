class StockSpanner:

    def __init__(self):
        self.top=0
        self.monostack=[]

    def next(self, price: int) -> int:
        temp=[]
        while self.monostack and self.monostack[-1][0]<=price:
            temp.append(self.monostack.pop())
        res= self.top+1 if not self.monostack else (self.top-self.monostack[-1][1])
        while temp:
            self.monostack.append(temp.pop())
        self.monostack.append((price,self.top))
        self.top+=1
        return res          


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)