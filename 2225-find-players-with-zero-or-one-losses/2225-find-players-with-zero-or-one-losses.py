from collections import defaultdict


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        wins, loses = defaultdict(int), defaultdict(int)
        for winner, loser in matches:
            wins[winner] += 1
            loses[loser] += 1
        zero_lose = [winner for winner in wins.keys() if loses[winner] == 0]
        one_lose = [loser for loser in loses.keys() if loses[loser] == 1]
        return [sorted(zero_lose), sorted(one_lose)]