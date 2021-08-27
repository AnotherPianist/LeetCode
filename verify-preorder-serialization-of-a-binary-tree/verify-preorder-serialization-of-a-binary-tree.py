class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        spaces = 1
        for node in preorder.split(','):
            if spaces == 0:
                return False
            elif node == '#':
                spaces -= 1
            else:
                spaces += 1
        return spaces == 0