from collections import Counter
from heapq import heapify, heappush, heappop


class Solution:
    def reorganizeString(self, s: str) -> str:
        res = []
        pq = [(-count, char) for char, count in Counter(s).items()]
        heapify(pq)

        while pq:
            count_first, char_first = heappop(pq)

            if not res or char_first != res[-1]:
                res.append(char_first)
                if count_first + 1 != 0:
                    heappush(pq, (count_first + 1, char_first))
            else:
                if not pq:
                    return ""
                count_second, char_second = heappop(pq)
                res.append(char_second)

                if count_second + 1 != 0:
                    heappush(pq, (count_second + 1, char_second))
                heappush(pq, (count_first, char_first))
        
        return "".join(res)