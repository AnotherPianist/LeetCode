from os.path import commonprefix


class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.characters = characters
        self.length = combinationLength
        self.state = ""

        
    def next(self) -> str:
        if self.state == "":
            self.state = self.characters[:self.length]
        else:
            end = len(commonprefix([self.characters[::-1], self.state[::-1]]))
            place = self.characters.index(self.state[-end - 1])
            self.state = self.state[:-end - 1] + self.characters[place + 1: place + 2 + end]
        return self.state
        

    def hasNext(self) -> bool:
        return self.state != self.characters[-self.length:]


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()