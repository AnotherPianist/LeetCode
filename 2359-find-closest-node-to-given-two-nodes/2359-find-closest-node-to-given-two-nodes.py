class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        
        def dfs(node, dist):
            d = 0
            while node != -1 and dist[node] == -1:
                dist[node] = d
                d += 1
                node = edges[node]
        
        
        dist1, dist2 = [-1] * len(edges), [-1] * len(edges)

        dfs(node1, dist1)
        dfs(node2, dist2)

        min_node, min_dist = -1, float("inf")
        for i in range(len(edges)):
            if dist1[i] >= 0 and dist2[i] >= 0 and max(dist1[i], dist2[i]) < min_dist:
                min_dist = max(dist1[i], dist2[i])
                min_node = i
        
        return min_node