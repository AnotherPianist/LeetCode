class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        prev_t, prev_c = releaseTimes[0], keysPressed[0]
        max_t, max_c = prev_t, prev_c
        for i in range(1, len(releaseTimes)):
            if releaseTimes[i] - releaseTimes[i - 1] > max_t:
                max_t, max_c = releaseTimes[i] - releaseTimes[i - 1], keysPressed[i]
            elif releaseTimes[i] - releaseTimes[i - 1] == max_t and keysPressed[i] > max_c:
                max_c = keysPressed[i]
        return max_c