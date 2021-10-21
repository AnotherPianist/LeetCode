from random import choice

class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.positions = {}
        

    def insert(self, val: int) -> bool:
        if val in self.positions:
            return False
        self.positions[val] = len(self.nums)
        self.nums.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.positions:
            return False
        idx = self.positions[val]
        self.positions[self.nums[-1]] = idx
        self.nums[idx], self.nums[-1] = self.nums[-1], self.nums[idx]
        self.nums.pop()
        del self.positions[val]
        return True
        

    def getRandom(self) -> int:
        return choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()