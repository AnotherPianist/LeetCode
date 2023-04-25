import heapq


class SmallestInfiniteSet:
    def __init__(self):
        self.is_present = set()
        self.added_integers = []
        self.current_integer = 1

    def popSmallest(self) -> int:
        if self.added_integers:
            smallest = heapq.heappop(self.added_integers)
            self.is_present.remove(smallest)
        else:
            smallest = self.current_integer
            self.current_integer += 1
        return smallest

    def addBack(self, num: int) -> None:
        if self.current_integer <= num or num in self.is_present:
            return
        heapq.heappush(self.added_integers, num)
        self.is_present.add(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)