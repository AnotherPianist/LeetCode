class SummaryRanges:

    def __init__(self):
        self.values = set()

    
    def addNum(self, value: int) -> None:
        self.values.add(value)


    def getIntervals(self) -> List[List[int]]:
        if not self.values:
            return [[], []]
        intervals = []
        left = right = -1
        for val in sorted(self.values):
            if intervals and val - intervals[-1][1] == 1:
                intervals[-1][1] = val
            else:
                intervals.append([val, val])
        return intervals


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()