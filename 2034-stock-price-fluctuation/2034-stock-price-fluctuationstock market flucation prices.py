import heapq

class StockPrice:

    def __init__(self):
        self.timestamp_price_map = {}
        self.latest_timestamp = 0
        self.min_heap = []
        self.max_heap = []

    def update(self, timestamp: int, price: int) -> None:
        self.timestamp_price_map[timestamp] = price
        self.latest_timestamp = max(self.latest_timestamp, timestamp)
        heapq.heappush(self.min_heap, (price, timestamp))
        heapq.heappush(self.max_heap, (-price, timestamp))

    def current(self) -> int:
        return self.timestamp_price_map[self.latest_timestamp]

    def maximum(self) -> int:
        while True:
            price, timestamp = self.max_heap[0]
            if -price == self.timestamp_price_map[timestamp]:
                return -price
            heapq.heappop(self.max_heap)

    def minimum(self) -> int:
        while True:
            price, timestamp = self.min_heap[0]
            if price == self.timestamp_price_map[timestamp]:
                return price
            heapq.heappop(self.min_heap)


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()