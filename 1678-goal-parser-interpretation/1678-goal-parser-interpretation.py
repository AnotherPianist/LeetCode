class Solution:
    def interpret(self, command: str) -> str:
        s = []
        
        i = 0
        while i < len(command):
            if command[i] == 'G':
                s.append('G')
                i += 1
            elif command[i + 1] == 'a':
                s.append("al")
                i += 4
            else:
                s.append("o")
                i += 2
                
        return "".join(s)