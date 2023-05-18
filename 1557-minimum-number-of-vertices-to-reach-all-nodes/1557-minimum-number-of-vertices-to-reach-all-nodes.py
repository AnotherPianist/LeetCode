class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        return set(edge[0] for edge in edges) - set(edge[1] for edge in edges)