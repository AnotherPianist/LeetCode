class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        if s == goal:
            count = [0] * 26
            
            for c in s:
                count[ord(c) - ord('a')] += 1
                if count[ord(c) - ord('a')] >= 2:
                    return True
            
            return False
        else:
            first = second = -1
            
            for i in range(len(s)):
                if s[i] != goal[i]:
                    if first == -1:
                        first = i
                    elif second == -1:
                        second = i
                    else:
                        return False
            
            if second == -1:
                return False
            
            return s[first] == goal[second] and s[second] == goal[first]