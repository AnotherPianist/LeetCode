class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = {}
        
        def recursion(dices, t):
            if dices == 0 and t == 0:
                return 1
            elif dices == 0 and t != 0:
                return 0
            if (dices, t) in dp:
                return dp[(dices, t)]
            s = 0
            for i in range(max(t - f, 0), t):
                s += recursion(dices - 1, i)
            dp[(dices, t)] = s
            return s
        
        return recursion(d, target) % (10 ** 9 + 7) 