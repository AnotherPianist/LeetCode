from collections import deque


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank_set = set(bank)
        queue = deque([start])
        seen = {start}
        
        steps = 0
        
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node == end:
                    return steps

                for c in "ACGT":
                    for i in range(len(node)):
                        mutation = node[:i] + c + node[i + 1:]
                        if mutation not in seen and mutation in bank_set:
                            queue.append(mutation)
                            seen.add(mutation)
            steps += 1

        return -1