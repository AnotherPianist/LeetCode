from collections import defaultdict, OrderedDict


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.freq2key = defaultdict(OrderedDict)
        self.key2freq = defaultdict(int)
        self.min_freq = 1
        

    def get(self, key: int) -> int:
        if key not in self.key2freq:
            return -1
        freq = self.key2freq[key]
        self.key2freq[key] += 1
        val = self.freq2key[freq][key]
        del self.freq2key[freq][key]
        self.freq2key[freq + 1][key] = val
        if freq == self.min_freq and not self.freq2key[freq]:
            self.min_freq += 1
        return val
        

    def put(self, key: int, value: int) -> None:
        if key in self.key2freq:
            self.get(key)
            self.freq2key[self.key2freq[key]][key] = value
        else:
            self.capacity -= 1
            self.key2freq[key] = 1
            self.freq2key[1][key] = value
            if self.capacity < 0:
                self.capacity += 1
                k, v = self.freq2key[self.min_freq].popitem(False)
                del self.key2freq[k]
            self.min_freq = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)